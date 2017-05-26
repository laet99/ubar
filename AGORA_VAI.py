import tkinter as tk
from PIL import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage

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
        soma = str(sum(self.conta))

    
    def pagar_conta(self, frame):
        f1.tkraise()
        frame.destroy()

		
    def mostrar(self, frame, nome,cardapio):
        frame.destroy()
        f3 = tk.Frame()
        f3.pack()
        f3.tkraise()   
        #background_label = Label(f3, image=filename)
        #background_label.place(x=0, y=0, relwidth=1, relheight=1)
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
        bt4 = tk.Button(f2, width=25, text="Dados Pagamento", command=lambda:self.Dados_pagamento(f2), font=fonte, bg="orange").pack()
        bt5 = tk.Button(f2, width=25, text="Ultimas Compras", command=lambda:self.Ultimas_compras(f2), font=fonte, bg="orange").pack()
        bt6 = tk.Button(f2, width=25, text="Informações Pessoais", command=lambda:self.Informacoes_pessoais(f2), font=fonte, bg="orange").pack()
        
        
    def criar_conta(self, frame):
        frame.destroy()
        f3 = tk.Frame()
        f3.pack()
        f3.tkraise()
        tk.Label(f3, text="Criar Conta", font=fonte2).grid()
        nome=tk.Entry(f3)
        nome.grid(row=1, column=1)
        nasc=tk.Entry(f3)
        nasc.grid(row=2, column=1)
        cpf=tk.Entry(f3)
        cpf.grid(row=3, column=1)
        mail=tk.Entry(f3)
        mail.grid(row=4, column=1)
        city=tk.Entry(f3)
        city.grid(row=6, column=1)
        rua=tk.Entry(f3)
        rua.grid(row=7, column=1)
        compl=tk.Entry(f3)
        compl.grid(row=8, column=1)
        ref=tk.Entry(f3)
        ref.grid(row=9, column=1)
        ncard=tk.Entry(f3)
        ncard.grid(row=11, column=1)
        nume=tk.Entry(f3)
        nume.grid(row=12, column=1)
        venc=tk.Entry(f3)
        venc.grid(row=13, column=1)
        code=tk.Entry(f3)
        code.grid(row=14, column=1)
        frase1 = tk.Label(f3, text="DADOS DO USUÁRIO")
        frase1.grid(row=0 , column=1)
        frase2 = tk.Label(f3, text="Nome")
        frase2.grid(row=1, column=0)
        frase3 = tk.Label(f3, text="Data de Nascimento")
        frase3.grid(row=2 , column=0)
        frase4 = tk.Label(f3, text="CPF")
        frase4.grid(row=3 , column=0)
        frase5 = tk.Label(f3, text="e-mail")
        frase5.grid(row=4 , column=0)
        frase6 = tk.Label(f3, text="ENDEREÇO DE COBRANÇA")
        frase6.grid(row=5 , column=1)
        frase7 = tk.Label(f3, text="Cidade")
        frase7.grid(row=6 , column=0)
        frase8 = tk.Label(f3, text="Rua")
        frase8.grid(row=7 , column=0)
        frase9 = tk.Label(f3, text="Complemento")
        frase9.grid(row=8 , column=0)
        frase11 = tk.Label(f3, text="Referência")
        frase11.grid(row=9 , column=0)
        frase12 = tk.Label(f3, text="DADOS DE PAGAMENTO")
        frase12.grid(row=10 , column=1)
        frase13 = tk.Label(f3, text="Nome (Como Impresso no Cartão)")
        frase13.grid(row=11 , column=0)
        frase14 = tk.Label(f3, text="Número do Cartão")
        frase14.grid(row=12 , column=0)
        frase15 = tk.Label(f3, text="Data de Vencimento")
        frase15.grid(row=13 , column=0)
        frase16 = tk.Label(f3, text="Código de Segurança")
        frase16.grid(row=14 , column=0)
        tk.Button(f3, text="Voltar Pagina Inicial", command=lambda:self.entrar(f3), font=fonte, bg="grey").grid()
        
    
    def Ultimas_compras(self, frame):
        frame.destroy()
        f4 = tk.Frame()
        f4.pack()
        f4.tkraise()
        tk.Label(f4, text="Ultimas Compras", font=fonte).pack()
        tk.Button(f4, text="Voltar Pagina Inicial", command=lambda:self.inicial(f4), font=fonte, bg="grey").pack()
        
     
    def Dados_pagamento (self, frame):
        frame.destroy()
        f5 = tk.Frame()
        f5.pack()
        f5.tkraise()
        tk.Label(f5, text="Dados Pagamento", font=fonte).pack()
        tk.Button(f5, text="Voltar Pagina Inicial", command=lambda:self.inicial(f5), font=fonte, bg="grey").pack()
        
    def entrar (self, frame):
        frame.destroy()
        f1 = tk.Frame()
        f1.pack()
        f1.tkraise()
        tk.Label(f1, text="UBAR", font=fonte3, fg="red").grid(row=0, column=2)
        tk.Label(f1, text="nome:").grid(row=2, column=1)
        tk.Entry(f1).grid(row=2, column=2)
        tk.Label(f1, text="senha:").grid(row=3, column=1)
        tk.Entry(f1).grid(row=3, column=2)
        tk.Button(f1, text="entrar",  command=lambda:self.inicial(f1), font=fonte).grid(row=4, column=2)
        tk.Label(f1, text="ainda não é cadastrado?").grid(row=6, column=3)
        tk.Button(f1, text="clique aqui", command=lambda:self.criar_conta(f1)).grid(row=6, column=4)



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
root.iconbitmap('favicon.ico')

#filename = PhotoImage(file = r"C:\\Users\\João Laet\\Documents\\desing de software\\breja.png")
#background_label = Label(root, image=filename)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)

f1 = tk.Frame()
f1.pack()
f1.tkraise()
tk.Label(f1, text="UBAR", font=fonte3, fg="red").grid(row=0, column=2)
tk.Label(f1, text="nome:").grid(row=2, column=1)
tk.Entry(f1).grid(row=2, column=2)
tk.Label(f1, text="senha:").grid(row=3, column=1)
tk.Entry(f1).grid(row=3, column=2)
tk.Button(f1, text="entrar",  command=lambda:bixo.inicial(f1), font=fonte).grid(row=4, column=2)
tk.Label(f1, text="ainda não é cadastrado?").grid(row=6, column=3)
tk.Button(f1, text="clique aqui", command=lambda:bixo.criar_conta(f1)).grid(row=6, column=4)
root.mainloop()
