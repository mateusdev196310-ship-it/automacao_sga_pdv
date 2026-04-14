from .logger import log

class AutomacaoBase:
    def __init__(self, caminho_exe: str, caminho_bd: str, usuario: str, senha: str):
        self.caminho_exe= caminho_exe
        self.caminho_bd= caminho_bd
        self.usuario= usuario
        self.senha= senha
        self.app= None
        self.janela= None

    def executar(self):
        raise NotImplementedError('Cada sistema deve implementar o método executar()')
