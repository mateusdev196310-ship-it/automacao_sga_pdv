# Digitação do login e senha

from pywinauto import Desktop,Application
from logger import log
import time
import win32gui
import win32process
import win32api

class Login:
    def __init__(self,janela,usuario: str,senha:str):
        self.janela=janela
        self.usuario=usuario
        self.senha=senha

    def fazer_login(self)->bool:
        
        try:

            if not self.janela.exists() or not self.janela.is_visible():
                log.info('Janela não está visível')
                return False
            
            log.info('Iniciando fluxo de login')

            campo_usuario= self.janela.child_window(class_name='TEdit', found_index=1)
            campo_senha= self.janela.child_window(class_name='TEdit', found_index=0)
            botao_entrar= self.janela.child_window(title='Entrar', class_name='TcxButton')

            foco_inicial= self.janela.has_focus()

           
            if not campo_usuario.has_focus():
                log.info('Campo usuário não está em foco')
                return False
            
            
            campo_usuario.type_keys("{TAB}")
            if campo_usuario.has_focus():
                log.info('Foco se manteve no campo login. Continuando fluxo')
                campo_usuario.set_text(self.usuario)
                log.info('Usuário preenchido')    
            else:
                log.info("Foco saiu do campo usuário sem preenchimento. Encerrando")
                return False
            
            campo_senha.type_keys("{ENTER}")
            if campo_senha.has_focus():
                log.info('Foco se manteve no campo senha. Continuando fluxo')
                campo_senha.set_text(self.senha)
                log.info('Senha preenchida')
            else:
                log.info("Foco saiu do campo senha sem preenchimento. Encerrando")
                return False

            

            botao_entrar.click()
            log.info('Botão Entrar clicado')

            time.sleep(10)

            # Verificar se a janela principal (Tform_Principal) abriu

            janelas=[i.class_name() for i in Desktop(backend='win32').windows()]
            

            if ('TForm_principal' in janelas):
                log.info('Login realizado com sucesso')
                return True
            else:
                log.info('Login falhou - Janela principal não identificada')
                return False
        
        except Exception as e:
            log.error(f"Erro no login: {type(e).__name__} - {e}")
            return False