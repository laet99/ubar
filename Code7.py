import tkinter as tk
from tkinter import Tk, StringVar, ttk

class Programa:

	def __init__(self,nome,cardapio):
		self.nome = nome
		self.cardapio = cardapio
		self.conta = []

	def conta(self, acumulado):
		self.acumulado += acumulado

	def adicionar(self, frame, comida, preco):
	   	item_carrinho = tk.Label(frame, text=("- "+comida), font=fontep)
	   	item_carrinho.pack()
	   	self.conta.append(preco)
	   	soma = sum(self.conta)

	def pagar_conta(self):
		global frame
		frame.destroy()
		f1.tkraise()
		   	
	def quit(self):
		f1.tkraise()

	def mostrar(self,frame):
	    frame.tkraise()
	    tk.Label(frame, text="Santo Pako", font=fonte3).pack()
	    notebook = ttk.Notebook(frame)
	    frame1 = ttk.Frame(notebook)
	    frame2 = ttk.Frame(notebook)
	    frame3 = ttk.Frame(notebook)
	    notebook.add(frame1, text='Cardápio')
	    notebook.add(frame2, text='Comanda')
	    notebook.add(frame3, text='Fechar Conta')
	    notebook.pack()
	    tk.Button(frame, text="Voltar Pagina Inicial", command=self.quit, font=fonte, bg="grey").pack()
	    tk.Label(frame1, text="Segue a baixo o cardápio do Santo Pako:", font=fonte).pack()
	    tk.Button(frame1, width=25, text=self.cardapio[0][0], font=fontep, command=lambda:self.adicionar(frame2,self.cardapio[0][0], self.cardapio[0][1])).pack()
	    tk.Button(frame1, width=25, text=self.cardapio[1][0], font=fontep, command=lambda:self.adicionar(frame2, self.cardapio[1][0], self.cardapio[1][1])).pack()
	    tk.Button(frame1, width=35, text=self.cardapio[2][0], font=fontep, command=lambda:self.adicionar(frame2, self.cardapio[2][0], self.cardapio[2][1])).pack()
	    tk.Label(frame2, text="Segue a baixo os seus pedidos ja feitos:", font=fonte).pack()
	    tk.Label(frame3, text="Segue a baixo sua conta:", font=fonte).pack()
	    tk.Button(frame3, text="pagar", font=fonte10, command=lambda:self.pagar_conta()).pack()

#Listas e fontes

cardapio_sujinhus = [["Skol Litão: R$9,00", 9],["Frangolone: R$6,00", 6],["Pastel: R$5,00", 5]]

cardapio_santo_pako = [["Torre de chopp: R$65,00", 65],["Sucão 5L: R$105,00", 105],["Batata Frita com Cheddar e Bacon R$27", 27]]

cardapio_bela_dama = [["Itaipava Litrão: R$7,00",7],["Provolone: R$34,00",34],["Polenta: R$19", 19]]

restaurantes = ["Santo Pako", "Sujinhus", "Bela Dama"]

fontep= ("Verdana", 8)
fonte10=("Verdana", 10)
fonte = ("Verdana", 12)
fonte3= ("Verdana", 20)
fonte2= ("Verdana", 16)

conta_visual = []

bixo = Programa("Bela Dama",cardapio_bela_dama)

bixo2 = Programa("Santo Pako",cardapio_santo_pako)

bixo3 = Programa("Sujinhus",cardapio_sujinhus)

root = tk.Tk()
root.geometry('700x600')
root.title("Ubar")

f1 = tk.Frame(root)
f2 = tk.Frame(root)
f3 = tk.Frame(root)
f4 = tk.Frame(root)
f5 = tk.Frame(root)
f6 = tk.Frame(root)
f7 = tk.Frame(root)

for frame in (f1, f2, f3, f4, f5, f6, f7):
    frame.grid(row=0, column=0, sticky='news') 
    
lb1 = tk.Label(f1, text="Qual bar você vai frequentar?", font=fonte2).pack(padx=210, pady=10)
bt1 = tk.Button(f1, width=25, text="Bela Dama", command=lambda:bixo.mostrar(f2), font=fonte, bg="red").pack()
bt2 = tk.Button(f1, width=25, text="Santo Pako", command=lambda:bixo2.mostrar(f3), font=fonte, bg="blue").pack()
bt3 = tk.Button(f1, width=25, text="Sujinhus", command=lambda:bixo3.mostrar(f4), font=fonte, bg="yellow").pack()
lb3 = tk.Label(f1, text="").pack()
lb2 = tk.Label(f1, text="Qual opção voce deseja acessar?", font=fonte2).pack()
bt4 = tk.Button(f1, width=25, text="Dados Pagamento", command=lambda:Dados_pagamento(f5), font=fonte, bg="orange").pack()
bt5 = tk.Button(f1, width=25, text="Ultimas Compras", command=lambda:Ultimas_compras(f6), font=fonte, bg="orange").pack()
bt6 = tk.Button(f1, width=25, text="Informações Pessoais", command=lambda:Informacoes_pessoais(f7), font=fonte, bg="orange").pack()


f1.tkraise()
root.mainloop()
