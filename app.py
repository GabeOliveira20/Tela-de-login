import customtkinter as ctk

# Configurar aparência
ctk.set_appearance_mode("dark")

# Função de validação
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    # Verificar se o usuário é Gabriel e a senha 1234
    if usuario == "Gabriel" and senha == "1234":
        resultado_login.configure(text="Login bem-sucedido!", text_color="green")
    else:
        resultado_login.configure(text="Usuário ou senha incorretos.", text_color="red")

# Criar janela principal
app = ctk.CTk()
app.title('Sistema de login')
app.geometry('400x300')

# Labels e campos
label_usuario = ctk.CTkLabel(app, text="Usuário:")
label_usuario.pack(pady=10)

campo_usuario = ctk.CTkEntry(app, placeholder_text="Digite seu usuário")
campo_usuario.pack(pady=10)

label_senha = ctk.CTkLabel(app, text="Senha:")
label_senha.pack(pady=10)

campo_senha = ctk.CTkEntry(app, placeholder_text="Digite sua senha", show="*")
campo_senha.pack(pady=10)

# Botão de login
botao_login = ctk.CTkButton(app, text="Login", command=validar_login)
botao_login.pack(pady=20)

# Campo feedback de login
resultado_login = ctk.CTkLabel(app, text="")
resultado_login.pack(pady=10)

# Iniciar aplicação
app.mainloop()