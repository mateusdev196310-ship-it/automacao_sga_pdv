from pywinauto import Desktop,Application

# janelas= Desktop(backend='win32')
# janelas=janelas.windows()



# classes=[]

# for w in janelas:
#     classes.append(w.class_name())

# print(classes)

app=Application(backend="win32").connect(class_name='TDlgSenha',timeout=5)
janela=app.window(class_name='TDlgSenha')

print(app)
print(janela)