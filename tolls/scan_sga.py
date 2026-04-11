

import time
from pywinauto import Application
from scan_componentes import scan_componentes

print("Você tem 5 segundos para abrir o SGA e deixar na tela desejada...")
time.sleep(5)

print("Conectando ao SGA...")

# conecta pelo nome do executável já aberto
app = Application(backend="win32").connect(path="SGA.exe")

print("Buscando janelas do processo...")

janelas = app.windows()

for janela in janelas:
    print(f"\nJanela encontrada: {janela.window_text()} | Classe: {janela.class_name()}")
    scan_componentes(janela)

print("\nScan finalizado.")