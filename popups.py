# Identificar/fechar janelas e popups que podem atrapalhar no fluxo da automação

from pywinauto import Desktop
from logger import log

class Popups:
    
    def __init__(self,app,janela):
        self.app=app
        self.janela=janela

    def fechar_popups(self):
        #Implemente verificação de popups
        return True