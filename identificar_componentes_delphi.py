from pywinauto import Application
import time

time.sleep(10)  # tempo pra você errar a senha manualmente

app = Application(backend="win32").connect(class_name="TDlgSenha")
janela = app.window(class_name="TDlgSenha")

for ctrl in janela.descendants():
    print(repr(ctrl.window_text()), "|", ctrl.class_name())