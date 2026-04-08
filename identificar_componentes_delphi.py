from pywinauto import Desktop, findwindows,Application
import time

time.sleep(5)

# for w in Desktop(backend="win32").windows():
#     print(w.window_text(), "|", w.class_name())



# janelas = findwindows.find_windows(title="TDlgSenha")
# print(janelas)  

app = Application(backend="win32").connect(class_name="TDlgSenha")
janela = app.window(class_name="TDlgSenha")
janela.print_control_identifiers()