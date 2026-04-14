# Identificar/fechar janelas e popups que podem atrapalhar no fluxo da automação

from infra.logger import log
import time

class Popups:
    
    def __init__(self, app, janela):
        self.app = app
        self.janela = janela

    def fechar_popups(self) -> bool:
        try:
            time.sleep(3)

            # Caso 1 — popup de backup
            janela_backup = self.app.window(title='Atenção!', class_name='#32770')
            if janela_backup.exists():
                log.info("Janela de backup identificada")
                botao_nao = janela_backup.child_window(title='&Não', class_name='Button')
                botao_nao.click()
                log.info("Popup de backup fechado")
                time.sleep(1)

            # Caso 2 — janela de nota pendente
            janela_nfce = self.app.window(class_name='TForm_ManuNFCe')
            if janela_nfce.exists():
                log.info("Janela de nota pendente identificada")
                janela_nfce.wait('visible', timeout=10)
                janela_nfce.type_keys('%{F4}')
                log.info('Fechando janela de nota pendente')
                time.sleep(1)

                janela_confirmacao = self.app.window(title='Atenção!', class_name='#32770')
                janela_confirmacao.wait('visible', timeout=10)
                botao_sim = janela_confirmacao.child_window(title='&Sim', class_name='Button')
                botao_sim.click()
                log.info('Janela de nota pendente fechada')

            log.info('Verificação de popups concluída')
            return True

        except Exception as e:
            log.error(f'Erro ao fechar popups: {type(e).__name__} - {e}')
            return False
