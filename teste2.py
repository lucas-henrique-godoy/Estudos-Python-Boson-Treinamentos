import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

def click_button():
    label.config(text="Botão clicado!")

# Criando a janela principal
root = tk.Tk()
root.title("Exemplo ttkbootstrap")

# Criando um estilo ttkbootstrap
style = Style(theme='flatly')

# Aplicando o estilo à janela principal
style.master.title('Exemplo ttkbootstrap')
style.master.iconbitmap(default='favicon.ico')

# Criando um Label
label = ttk.Label(root, text="Olá, ttkbootstrap!", style='info.TLabel')
label.pack(pady=10)

# Criando um Botão
button = ttk.Button(root, text="Clique Aqui!", command=click_button, style='success.TButton')
button.pack()

# Loop principal para exibir a janela
root.mainloop()
