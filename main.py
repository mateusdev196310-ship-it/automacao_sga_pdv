"""Ponto de entrada: seleção de fluxos, execução e relatório final."""

from automacao_sga import AutomacaoSGA
import configparser
import os
import sys
from logger import log



if __name__ == '__main__':

    config=configparser.ConfigParser()
    config.read('config.ini',encoding='utf8')

    caminho_exe = config['SGA']['caminho_exe']
    caminho_bd = config['SGA']['caminho_bd']
    usuario = config['SGA']['usuario']
    senha = config['SGA']['senha']

    sga = AutomacaoSGA(caminho_exe,caminho_bd,usuario,senha)
    sga.executar()