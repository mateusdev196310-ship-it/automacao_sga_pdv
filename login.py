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
                log.error('Janela não está visível')
                return False
            
            log.info('Iniciando fluxo de login')

            campo_usuario= self.janela.child_window(class_name='TEdit', found_index=1)
            campo_senha= self.janela.child_window(class_name='TEdit', found_index=0)
            botao_entrar= self.janela.child_window(title='Entrar', class_name='TcxButton')

            foco_antes= self._obter_foco()
            if not foco_antes:
                log.error('Nenhum controle está em foco')
                return False
            
            campo_usuario.type_keys("{TAB}")
            time.sleep(0.5)
            foco_depois= self._obter_foco()

            if not foco_antes == foco_depois:
                log.error("Foco mudou do campo usuário sem inserção de caractere")
                return False
            log.info("TAB pressionado sem usuário — foco mantido no campo usuário | Comportamento esperado")
            
            campo_usuario.set_text(self.usuario)
            campo_usuario.type_keys("{TAB}")
            time.sleep(0.5)

            foco_depois= self._obter_foco()
            if foco_antes == foco_depois:
                log.error('Foco não mudou do campo usuário após digitar usuário e apertar tab')
                return False
            log.info("TAB pressionado com usuário preenchido — foco moveu para o campo senha | Comportamento esperado")
            
            foco_antes=self._obter_foco()
            campo_senha.type_keys("{ENTER}")
            time.sleep(0.5)
            foco_depois=self._obter_foco()
            if not foco_antes == foco_depois:
                log.error('Foco mudou do campo senha sem inserção de caractere')
                return False
            log.info("ENTER pressionado sem senha — foco mantido no campo senha | Comportamento esperado")
            
            campo_senha.set_text(self.senha)
            campo_senha.type_keys("{TAB}")
            foco_depois= self._obter_foco()

            if foco_antes==foco_depois:
                log.error('Foco não mudou do campo senha após digitar senha e apertar tab')
                return False
            log.info("TAB pressionado com senha preenchida — foco moveu para botão Entrar | Comportamento esperado")
            
            botao_entrar.click()
            log.info('Botão Entrar clicado')

            time.sleep(10)

            # Verificar se a janela principal (Tform_Principal) abriu

            janelas=[i.class_name() for i in Desktop(backend='win32').windows()]
            

            if ('TForm_principal' in janelas):
                log.info('Login realizado com sucesso')
                return True
            else:
                log.error('Login falhou - Janela principal não identificada')
                return False
        
        except Exception as e:
            log.error(f"Erro no login: {type(e).__name__} - {e}")
            return False
        
    def _obter_foco(self):
        hwnd= win32gui.GetForegroundWindow() # Pega o handle da janela queestá  em primeiro plano
        thread_id = win32process.GetWindowThreadProcessId(hwnd)[0]
        win32process.AttachThreadInput(win32api.GetCurrentThreadId(),thread_id,True)
        focused= win32gui.GetFocus()
        win32process.AttachThreadInput(win32api.GetCurrentThreadId(),thread_id,False)
        return focused
