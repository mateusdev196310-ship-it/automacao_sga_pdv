import time
from pywinauto import Application

print("Você tem 5 segundos para abrir o SGA...")
time.sleep(5)

print("Conectando ao SGA...")
app = Application(backend="win32").connect(path="SGA.exe")

print("Listando janelas visíveis do processo...\n")

for w in app.windows():
    try:
        if w.is_visible():
            print("===================================")
            print(f"Título : {w.window_text()}")
            print(f"Classe : {w.class_name()}")
            print(f"Handle : {w.handle}")
            print("===================================\n")
    except Exception as e:
        print(f"Erro ao acessar janela: {e}")

print("Fim da listagem.")