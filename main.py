"""Ponto de entrada: seleção de fluxos, execução e relatório final."""

from automacao_sga import AutomacaoSGA
from logger import log



if __name__ == '__main__':
    sga = AutomacaoSGA('C:\\Users\\mateussouza\\Desktop\\QA\\SGA\\sac4win\\SGA.exe',
                       'C:\\Users\\mateussouza\\Desktop\\QA\\SGA\\sac4win\\dados\\SAC4WIN.FDB',
                       '1','1')
    sga.executar()