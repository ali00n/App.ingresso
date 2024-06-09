from tkinter import *
from tkinter import messagebox

def verificar_compra():
    nome = nomeValue.get()
    idade = int(idadeValue.get())
    ingresso = ingresso_var.get()
    
    if idade < 18:
        messagebox.showwarning("Compra não permitida", "Você precisa ter pelo menos 18 anos para comprar um ingresso.")
    else:
        messagebox.showinfo("Compra realizada", f"Parabéns, {nome}! Você comprou um ingresso do tipo {ingresso}.")

janela = Tk()

janela.title("Loja de ingressos")
janela.grid_rowconfigure(0, weight=1)
janela.grid_rowconfigure(1, weight=1)
janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)

nome = Label(janela, text="Seu nome: ")
nome.grid(row=0, column=0, pady=10, padx=10, sticky="w")

nomeValue = Entry(janela, width=20)
nomeValue.grid(row=0, column=1, pady=10, padx=10, sticky="ew")

idade = Label(janela, text="Digite sua idade: ")
idade.grid(row=1, column=0, pady=10, padx=10, sticky="w")

idadeValue = Entry(janela, width=20)
idadeValue.grid(row=1, column=1, pady=10, padx=10, sticky="ew")

compra_ingresso = Label(janela, text="Escolha qual ingresso irá querer: ")
compra_ingresso.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky="w")

ingresso_var = StringVar(value="Pista")

ingresso_pista = Radiobutton(janela, text="Pista 100R$", variable=ingresso_var, value="Pista")
ingresso_pista.grid(row=3, column=0, pady=5, padx=10, sticky="w")

ingresso_camarote = Radiobutton(janela, text="Camarote 500R$", variable=ingresso_var, value="Camarote")
ingresso_camarote.grid(row=3, column=1, pady=5, padx=10, sticky="w")

botao = Button(janela, text="Comprar", command=verificar_compra, bg="#007BFF", fg="#ffffff", font=("Arial", 12))
botao.grid(row=4, column=0, columnspan=2, pady=20, sticky="ew")

janela.columnconfigure(0, weight=1)
janela.columnconfigure(1, weight=1)
janela.rowconfigure(0, weight=1)
janela.rowconfigure(1, weight=1)

janela.mainloop()
