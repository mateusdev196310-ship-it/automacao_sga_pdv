"""Rotinas de automação do SGA ."""

from base import AutomacaoBase
from abrir_sga import GerenciadorSGA
from login import Login
from popups import Popups
from logger import log

class AutomacaoSGA(AutomacaoBase):


    def executar(self)->bool:
        log.criar_arquivo_log('TXT')
        
        #Abrir SGA
        sga= GerenciadorSGA(self.caminho_exe,self.caminho_bd,self.usuario,self.senha)
        

        if not sga.abrir_sga():
            log.error("Falha na abertura do SGA. Encerrando")
            return False
        
        self.app= sga.app
        self.janela= sga.janela

        #login
        login=Login(self.janela, self.usuario,self.senha)

        if not login.fazer_login():
            log.error("Falha no login. Encerrando")
            return False
        
        #Tratar/fechar popups e janelas
        
        popups = Popups(self.app,self.janela)

        if not popups.fechar_popups():
            log.info('Falha na verificação de popups. Encerrando')

        #Navegação até rotinas do SGA
        ...
        

        #Entrada de produtos

        return True

