# Digitação do login e senha

from pywinauto import Desktop
from infra.logger import log
import time
import win32gui
import win32process
import win32api

class Login:
    def __init__(self, app ,janela, usuario: str, senha: str):
        self.app=app
        self.janela = janela
        self.usuario = usuario
        self.senha = senha

    def fazer_login(self) -> bool:
        try:
            if not self.janela.exists() or not self.janela.is_visible():
                log.error('Janela não está visível')
                return False

            log.info('Iniciando fluxo de login')

            campo_usuario = self.janela.child_window(class_name='TEdit', found_index=1)
            campo_senha = self.janela.child_window(class_name='TEdit', found_index=0)
            botao_entrar = self.janela.child_window(title='Entrar', class_name='TcxButton')

            # campo_usuario.click()

            #Validação de foco

            if self._obter_foco() != campo_usuario.handle:
                log.error('Foco não está no campo usuário')
                return False

            campo_usuario.type_keys("{TAB}")
            time.sleep(0.5)
            if self._obter_foco() != campo_usuario.handle:
                log.error('Foco mudou do campo usuário sem inserção de caractere')
                return False
            log.info("TAB pressionado sem usuário — foco mantido no campo usuário | Comportamento esperado")

            campo_usuario.set_text(self.usuario)
            campo_usuario.type_keys("{TAB}")
            time.sleep(0.5)
            if self._obter_foco() == campo_usuario.handle:
                log.error('Foco não mudou do campo usuário após digitar usuário e apertar tab')
                return False
            log.info("TAB pressionado com usuário preenchido — foco moveu para campo senha | Comportamento esperado")

            campo_senha.type_keys("{ENTER}")
            time.sleep(0.5)
            if self._obter_foco() != campo_senha.handle:
                log.error('Foco mudou do campo senha sem inserção de caractere')
                return False
            log.info("ENTER pressionado sem senha — foco mantido no campo senha | Comportamento esperado")

            campo_senha.set_text(self.senha)
            campo_senha.type_keys("{TAB}")
            time.sleep(0.5)
            if self._obter_foco() == campo_senha.handle:
                log.error('Foco não mudou do campo senha após digitar senha e apertar tab')
                return False
            log.info("TAB pressionado com senha preenchida — foco moveu para botão Entrar | Comportamento esperado")

            botao_entrar.click()
            log.info('Botão Entrar clicado')


            try:
                janela_principal= self.app.window(class_name='TForm_principal')
                janela_principal.wait('exists enabled visible ready',timeout=20)
                log.info("Login realizado com sucesso")
                log.info('Janela principal do SGA visível')
                return True
            except Exception as e:
                log.error(f"Janela principal do SGA não identificada {e}")
                return False    
            

        except Exception as e:
            log.error(f"Erro no login: {type(e).__name__} - {e}")
            return False

    def _obter_foco(self):
        hwnd = win32gui.GetForegroundWindow()
        thread_id = win32process.GetWindowThreadProcessId(hwnd)[0]
        win32process.AttachThreadInput(win32api.GetCurrentThreadId(), thread_id, True)
        focused = win32gui.GetFocus()
        win32process.AttachThreadInput(win32api.GetCurrentThreadId(), thread_id, False)
        return focused
