# Abertura do SGA.exe e vaidação de abertura

import time
import os
import subprocess
import psutil
from pywinauto import Application,Desktop
from pywinauto.findwindows import ElementNotFoundError
from logger import log

class GerenciadorSGA:
    

    def __init__(self, caminho_exe: str,caminho_bd: str, usuario: str, senha:str):
        self.caminho_exe=caminho_exe
        self.caminho_bd=caminho_bd
        self.usuario=usuario
        self.senha=senha
        self.app=None
        self.janela= None
        
    def abrir_sga(self) -> bool:
        
        
        try:
            if not os.path.exists(self.caminho_exe):
                log.error(f'Executável não encontrado no caminho : {self.caminho_exe}')
                return False
            
            self.fechar_instancias_anteriores()
            
            pasta_exe = os.path.dirname(self.caminho_exe)
            log.info(f'Abrindo SGA: {self.caminho_exe}')
            subprocess.Popen([self.caminho_exe], cwd=pasta_exe)

            log.info("Aguardando SGA abrir (10 segundos)...")
            time.sleep(10)

            janelas= Desktop(backend='win32').windows()
            classes=[w.class_name() for w in janelas]

            if 'TDlgSenha' in classes:
                # ponte para conexão com o processo do SGA (aplicação Windows já aberta)
                self.app=Application(backend="win32").connect(class_name='TDlgSenha',timeout=15)
                # referência para a janela específica de senha dentro do SGA
                self.janela=self.app.window(class_name='TDlgSenha')
                log.info('Janela de login identificada com sucesso')
                return True
                
            
            elif 'TSplash' in classes:
                log.error('Verifique a configuração do banco de dados ou a versão do firebird instalada')
                return False
            else:
                log.info('Janela de login não identificada identificada')
                return False

            
        except PermissionError as e:
            log.error(f'Erro de permissão ao abrir SGA: {e}')
            return False
        
        except FileNotFoundError as e:
            log.error(f'Arquivo não encontrado: {e}')
            return False
        
        except Exception as e:
            log.error(f'Erro inesperado: {type(e).__name__} - {e}')
            return False
    
    def fechar_instancias_anteriores(self):
        for processo in psutil.process_iter(['name']):
            if processo.name() == 'SGA.exe':
                  log.info("Instância anterior do SGA encontrada, encerrando...")
                  processo.terminate()

                  try:
                      processo.wait(timeout=5)

                  except psutil.TimeoutExpired:
                      log.info('Processo não encerrado. Forçando kill')
                      processo.kill()
                       
                  time.sleep(2)
                  log.info("Instância encerrada.")
            

    
#Retornar no fluxo de inserção dos caminhos, criar arquivo config.py  

