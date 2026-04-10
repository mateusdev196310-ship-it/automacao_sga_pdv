# from pywinauto import Application
# import time

# time.sleep(3)

# app = Application(backend="win32").connect(class_name="TDlgSenha")
# janela = app.window(class_name="TDlgSenha")
# janela.print_control_identifiers(depth=10)

# from pywinauto import Desktop
# import time

# time.sleep(3)

# foco_atual = Desktop(backend='win32').get_focus()
# print(foco_atual)



# from pywinauto import Application
# import time

# time.sleep(3)
# app = Application(backend="win32").connect(class_name="TDlgSenha")
# janela = app.window(class_name="TDlgSenha")

# campo_usuario = janela.child_window(class_name="TEdit", found_index=1)
# campo_senha = janela.child_window(class_name="TEdit", found_index=0)

# print("Usuário em foco:", campo_usuario.has_focus())
# print("Senha em foco:", campo_senha.has_focus())

from pywinauto import Application
import win32gui
import win32process
import win32api
import time

time.sleep(3)
app = Application(backend="win32").connect(class_name="TDlgSenha")
janela = app.window(class_name="TDlgSenha")
campo_usuario = janela.child_window(class_name="TEdit", found_index=1)

def get_focused_hwnd():
    hwnd = win32gui.GetForegroundWindow()
    thread_id = win32process.GetWindowThreadProcessId(hwnd)[0]
    win32process.AttachThreadInput(win32api.GetCurrentThreadId(), thread_id, True)
    focused = win32gui.GetFocus()
    win32process.AttachThreadInput(win32api.GetCurrentThreadId(), thread_id, False)
    return focused

campo_usuario.set_text("1")
time.sleep(0.3)

antes = get_focused_hwnd()
print("Antes:", antes)

campo_usuario.type_keys("{TAB}")
time.sleep(0.3)

depois = get_focused_hwnd()
print("Depois:", depois)

print("Foco mudou:", antes != depois)