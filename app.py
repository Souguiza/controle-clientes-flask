import sqlite3
import tkinter as tk
from tkinter import messagebox

# Função para criar o banco de dados e a tabela, se não existirem
def criar_banco():
    conn = sqlite3.connect('banco_dados.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY,
                        nome TEXT NOT NULL,
                        email TEXT NOT NULL);''')
    conn.commit()
    conn.close()

# Função para adicionar usuário ao banco de dados
def adicionar_usuario(nome, email):
    if nome == "" or email == "":
        messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos!")
        return

    conn = sqlite3.connect('banco_dados.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucesso", "Usuário adicionado com sucesso!")
    limpar_campos()

# Função para exibir todos os usuários
def exibir_usuarios():
    conn = sqlite3.connect('banco_dados.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios

# Função para limpar os campos de entrada
def limpar_campos():
    nome_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

# Função para atualizar a lista de usuários na UI
def atualizar_lista():
    for widget in lista_frame.winfo_children():
        widget.destroy()

    usuarios = exibir_usuarios()
    for usuario in usuarios:
        usuario_label = tk.Label(lista_frame, text=f"ID: {usuario[0]} - Nome: {usuario[1]} - Email: {usuario[2]}")
        usuario_label.pack()

# Configuração da janela principal
root = tk.Tk()
root.title("Gerenciamento de Usuários")

# Tamanho da janela
root.geometry("500x400")

# Criando banco de dados
criar_banco()

# Label e entrada para o nome
nome_label = tk.Label(root, text="Nome:")
nome_label.pack()
nome_entry = tk.Entry(root, width=40)
nome_entry.pack()

# Label e entrada para o email
email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root, width=40)
email_entry.pack()

# Botão para adicionar usuário
adicionar_btn = tk.Button(root, text="Adicionar Usuário", command=lambda: adicionar_usuario(nome_entry.get(), email_entry.get()))
adicionar_btn.pack(pady=10)

# Frame para exibir a lista de usuários
lista_frame = tk.Frame(root)
lista_frame.pack(pady=10)

# Botão para atualizar a lista de usuários
atualizar_btn = tk.Button(root, text="Atualizar Lista", command=atualizar_lista)
atualizar_btn.pack(pady=10)

# Rodando a aplicação
root.mainloop()