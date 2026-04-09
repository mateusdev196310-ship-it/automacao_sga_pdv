# from pywinauto import Application
# import time

# time.sleep(5)

# app = Application(backend="win32").connect(class_name="TDlgSenha")
# janela = app.window(class_name="TDlgSenha")
# janela.print_control_identifiers()

from pywinauto import Desktop
import time

time.sleep(5)
for w in Desktop(backend="win32").windows():
    print(repr(w.window_text()), "|", w.class_name())