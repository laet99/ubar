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
        conta.append(preco)
        soma = str(sum(self.conta))

    
    def pagar_conta(self, frame):
        f1.tkraise()
        frame.destroy()


    def mostrar(self, frame, nome,cardapio):
        frame.destroy()
        f3 = tk.Frame()
        f3.pack()
        f3.tkraise()          
        tk.Label(f3, text=nome, font=fonte3).pack()
        notebook = ttk.Notebook(f3)
        frame1 = ttk.Frame(notebook)
        frame2 = ttk.Frame(notebook)
        frame3 = ttk.Frame(notebook)
        notebook.add(frame1, text='Cardápio')
        notebook.add(frame2, text='Comanda')
        notebook.add(frame3, text='Fechar Conta')
        notebook.pack()
        tk.Button(f3, text="Voltar Pagina Inicial", command=lambda:self.inicial(f3), font=fonte, bg="grey").pack()
        tk.Label(frame1, text="Segue a baixo o cardápio do "+nome+":", font=fonte).pack()
        tk.Button(frame1, width=25, text=cardapio[0][0], font=fontep, command=lambda:self.adicionar(frame2,cardapio[0][0],cardapio[0][1])).pack()
        tk.Button(frame1, width=25, text=cardapio[1][0], font=fontep, command=lambda:self.adicionar(frame2, cardapio[1][0],cardapio[1][1])).pack()
        tk.Button(frame1, width=35, text=cardapio[2][0], font=fontep, command=lambda:self.adicionar(frame2, cardapio[2][0],cardapio[2][1])).pack()
        tk.Label(frame2, text="Segue a baixo os seus pedidos ja feitos: ", font=fonte).pack()
        tk.Label(frame3, text=("Sua conta foi de: ")).pack()
        tk.Button(frame3, text="pagar", font=fonte10, command=lambda:self.pagar_conta()).pack()

        
    def inicial(self, frame):
        frame.destroy()
        f2 = tk.Frame()
        f2.pack()
        f2.tkraise()
        lb1 = tk.Label(f2, width=50, text="Qual bar você vai frequentar?", font=fonte2).pack(padx=150, pady=10)
        bt1 = tk.Button(f2, width=25, text="Bela Dama", command=lambda:self.mostrar(f2, "Bella Dama", cardapio_bela_dama), font=fonte, bg="red").pack()
        bt2 = tk.Button(f2, width=25, text="Santo Pako", command=lambda:self.mostrar(f2, "Santo Pako", cardapio_santo_pako), font=fonte, bg="red").pack()
        bt3 = tk.Button(f2, width=25, text="Sujinhus", command=lambda:self.mostrar(f2, "Sujinhus", cardapio_sujinhus), font=fonte, bg="red").pack()
        lb3 = tk.Label(f2, text="").pack()
        lb2 = tk.Label(f2, text="Qual opção voce deseja acessar?", font=fonte2).pack()
        bt4 = tk.Button(f2, width=25, text="Dados Pagamento", command=lambda:Dados_pagamento(), font=fonte, bg="orange").pack()
        bt5 = tk.Button(f2, width=25, text="Ultimas Compras", command=lambda:Ultimas_compras(), font=fonte, bg="orange").pack()
        bt6 = tk.Button(f2, width=25, text="Informações Pessoais", command=lambda:Informacoes_pessoais(), font=fonte, bg="orange").pack()

cardapio_sujinhus = [["Skol Litão: R$9,00", 9],["Frangolone: R$6,00", 6],["Pastel: R$5,00", 5]]
cardapio_santo_pako = [["Torre de chopp: R$65,00", 65],["Sucão 5L: R$105,00", 105],["Batata Frita com Cheddar e Bacon R$27", 27]]
cardapio_bela_dama = [["Itaipava Litrão: R$7,00",7],["Provolone: R$34,00",34],["Polenta: R$19", 19]] 

fontep= ("Verdana", 8)
fonte10=("Verdana", 10)
fonte = ("Verdana", 12)
fonte3= ("Verdana", 20)
fonte2= ("Verdana", 16)
       
bixo = Programa("Bela Dama",cardapio_bela_dama)

root = tk.Tk()
root.geometry('700x600')
root.title("Ubar")
f1 = tk.Frame()
f1.pack()
tk.Label(f1, text="UBAR", font=fonte3, fg="red").pack()
tk.Button(f1, text="Entrar na diverssão",  command=lambda:bixo.inicial(f1), font=fonte).pack()
root.mainloop()