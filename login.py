# Digitação do login e senha

from pywinauto import Desktop
from logger import log
import time


class Login:
    def __init__(self,janela,usuario: str,senha:str):
        self.janela=janela
        self.usuario=usuario
        self.senha=senha

    def fazer_login(self)->bool:
        
        try:

            log.info('Iniciando fluxo de login')

            campo_usuario= self.janela.child_window(class_name='TEdit', found_index=1)
            campo_senha= self.janela.child_window(class_name='TEdit', found_index=2)
            botao_entrar= self.janela.child_window(title='Entrar', class_name='TcxButton')

            campo_usuario.set_text(self.usuario)
            log.info('Usuário preenchido')

            campo_senha.set_text(self.senha)
            log.info('Senha preenchida')

            botao_entrar.click()
            log.info('Botão Entrar clicado')

            time.sleep(7)

            # Verificar se a janela principal (Tform_Principal) abriu

            janelas=[i.class_name() for i in Desktop(backend='win32').windows()]

            if 'Tform_Principal' in janelas:
                log.info('Login realizado com sucesso')
                return True
            else:
                log.info('Login falhou - Janela principal não identificada')
                return False
        
        except Exception as e:
            log.error(f"Erro no login: {type(e).__name__} - {e}")
            return False