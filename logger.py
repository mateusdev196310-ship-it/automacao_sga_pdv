"""Logging do projeto e exportação de relatórios (TXT/CSV)."""

import logging
import sys
import queue
import threading
import datetime
import csv
import os
import json
from collections import defaultdict
from typing import List

from utils import formatar_moeda_br, formatar_numero_br


class SistemaLogging:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._inicializar()
        return cls._instance
    
    def _inicializar(self):
        self.logger = logging.getLogger("AutomacaoNF")
        self.logger.setLevel(logging.DEBUG)
        self.logger.handlers = []
        
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_format = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | %(message)s',
            datefmt='%H:%M:%S'
        )
        console_handler.setFormatter(console_format)
        self.logger.addHandler(console_handler)
        
        self.file_handler = None
        self.caminho_log = None
        self.queue = queue.Queue()
        self.worker_thread = threading.Thread(target=self._processar_fila, daemon=True)
        self.worker_thread.start()
        self.metricas = []
        self.eventos = []
    
    def criar_arquivo_log(self, formato: str = 'txt') -> str:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if formato.upper() == 'TXT':
            filename = f"log_automacao_nf_{timestamp}.txt"
            self.file_handler = logging.FileHandler(filename, encoding='utf-8')
            self.file_handler.setLevel(logging.DEBUG)
            file_format = logging.Formatter(
                '%(asctime)s | %(levelname)-8s | %(funcName)-20s | %(message)s',
                datefmt='%d/%m/%Y %H:%M:%S'
            )
            self.file_handler.setFormatter(file_format)
            self.logger.addHandler(self.file_handler)
        else:
            filename = f"log_automacao_nf_{timestamp}.{formato.lower()}"
        
        self.caminho_log = filename
        self.info(f"Log iniciado: {filename} (Formato: {formato})")
        return filename
    
    def _processar_fila(self):
        while True:
            try:
                level, msg, extra = self.queue.get(timeout=1)
                if level == 'info':
                    self.logger.info(msg)
                elif level == 'error':
                    self.logger.error(msg)
                elif level == 'warning':
                    self.logger.warning(msg)
                elif level == 'debug':
                    self.logger.debug(msg)
                
                self.eventos.append({
                    'timestamp': datetime.datetime.now().isoformat(),
                    'level': level,
                    'mensagem': msg,
                    'extra': extra
                })
            except queue.Empty:
                continue
    
    def info(self, msg: str, extra: dict = None):
        self.queue.put(('info', msg, extra))
    
    def error(self, msg: str, extra: dict = None):
        self.queue.put(('error', msg, extra))
    
    def warning(self, msg: str, extra: dict = None):
        self.queue.put(('warning', msg, extra))
    
    def debug(self, msg: str, extra: dict = None):
        self.queue.put(('debug', msg, extra))
    
   

# Instância global do logger
log = SistemaLogging()
