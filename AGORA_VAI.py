import tkinter as tk
from PIL import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import StringVar

def adicionar(frame, comida, preco):
    global soma
    item_carrinho = tk.Label(frame, text=("- "+comida), font=fontep)
    item_carrinho.pack()
    conta.append(preco)
    soma = str(sum(conta))
    conta_final.config(text="Sua conta é de " + soma + ",00R$")


def mostrar(frame, nome, cardapio):
    global conta_final
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
    tk.Label(frame1, text="Segue a baixo o cardápio do "+nome+":", font=fonte).pack()
    tk.Button(frame1, width=25, text=cardapio[0][0], font=fontep, command=lambda:adicionar(frame2,cardapio[0][0],cardapio[0][1])).pack()
    tk.Button(frame1, width=25, text=cardapio[1][0], font=fontep, command=lambda:adicionar(frame2, cardapio[1][0],cardapio[1][1])).pack()
    tk.Button(frame1, width=35, text=cardapio[2][0], font=fontep, command=lambda:adicionar(frame2, cardapio[2][0],cardapio[2][1])).pack()
    tk.Label(frame2, text="Segue a baixo os seus pedidos ja feitos: ", font=fonte).pack()
    conta_final = tk.Label(frame3, text=("Você ainda não consumiu nada."))
    conta_final.pack()
    b1 = tk.Button(frame3, text="pagar", command=lambda:inicial1(f3), font=fonte10)
    b2 = tk.Button(f3, text="Voltar Pagina Inicial", command=lambda:inicial2(f3), font=fonte, bg="grey")
    b1.pack()
    b2.pack()
    
    
def inicial1(frame):
    global conta
    if sum(conta) > 0:
        conta = []
        frame.destroy()
        f2 = tk.Frame()
        f2.pack()
        f2.tkraise()
        lb1 = tk.Label(f2, width=50, text="Qual bar você vai frequentar?", font=fonte2).pack(padx=150, pady=10)
        bt1 = tk.Button(f2, width=25, text="Bela Dama", command=lambda:mostrar(f2, "Bella Dama", cardapio_bela_dama), font=fonte, bg="red").pack()
        bt2 = tk.Button(f2, width=25, text="Santo Pako", command=lambda:mostrar(f2, "Santo Pako", cardapio_santo_pako), font=fonte, bg="red").pack()
        bt3 = tk.Button(f2, width=25, text="Sujinhus", command=lambda:mostrar(f2, "Sujinhus", cardapio_sujinhus), font=fonte, bg="red").pack()
        lb3 = tk.Label(f2, text="").pack()
        lb2 = tk.Label(f2, text="Qual opção voce deseja acessar?", font=fonte2).pack()
        bt5 = tk.Button(f2, width=25, text="Ultimas Compras", command=lambda:Ultimas_compras(f2), font=fonte, bg="orange").pack()
        bt6 = tk.Button(f2, width=25, text="Informações Pessoais", command=lambda:informacoes_pessoais(f2), font=fonte, bg="orange").pack()


def inicial2(frame):
    global conta
    if sum(conta) == 0:
        conta = []
        frame.destroy()
        f2 = tk.Frame()
        f2.pack()
        f2.tkraise()
        lb1 = tk.Label(f2, width=50, text="Qual bar você vai frequentar?", font=fonte2).pack(padx=150, pady=10)
        bt1 = tk.Button(f2, width=25, text="Bela Dama", command=lambda:mostrar(f2, "Bella Dama", cardapio_bela_dama), font=fonte, bg="red").pack()
        bt2 = tk.Button(f2, width=25, text="Santo Pako", command=lambda:mostrar(f2, "Santo Pako", cardapio_santo_pako), font=fonte, bg="red").pack()
        bt3 = tk.Button(f2, width=25, text="Sujinhus", command=lambda:mostrar(f2, "Sujinhus", cardapio_sujinhus), font=fonte, bg="red").pack()
        lb3 = tk.Label(f2, text="").pack()
        lb2 = tk.Label(f2, text="Qual opção voce deseja acessar?", font=fonte2).pack()
        bt5 = tk.Button(f2, width=25, text="Ultimas Compras", command=lambda:Ultimas_compras(f2), font=fonte, bg="orange").pack()
        bt6 = tk.Button(f2, width=25, text="Informações Pessoais", command=lambda:informacoes_pessoais(f2), font=fonte, bg="orange").pack()


def inicial(frame):
    global conta
    usuario_final = usuario.get()
    senha_final2 = senha.get()
    if usuario_final == nome_final and senha_final == senha_final2:
        conta = []
        frame.destroy()
        f2 = tk.Frame()
        f2.pack()
        f2.tkraise()
        lb1 = tk.Label(f2, width=50, text="Qual bar você vai frequentar?", font=fonte2).pack(padx=150, pady=10)
        bt1 = tk.Button(f2, width=25, text="Bela Dama", command=lambda:mostrar(f2, "Bella Dama", cardapio_bela_dama), font=fonte, bg="red").pack()
        bt2 = tk.Button(f2, width=25, text="Santo Pako", command=lambda:mostrar(f2, "Santo Pako", cardapio_santo_pako), font=fonte, bg="red").pack()
        bt3 = tk.Button(f2, width=25, text="Sujinhus", command=lambda:mostrar(f2, "Sujinhus", cardapio_sujinhus), font=fonte, bg="red").pack()
        lb3 = tk.Label(f2, text="").pack()
        lb2 = tk.Label(f2, text="Qual opção voce deseja acessar?", font=fonte2).pack()
        bt5 = tk.Button(f2, width=25, text="Ultimas Compras", command=lambda:Ultimas_compras(f2), font=fonte, bg="orange").pack()
        bt6 = tk.Button(f2, width=25, text="Informações Pessoais", command=lambda:informacoes_pessoais(f2), font=fonte, bg="orange").pack()


def inicial3 (frame):
    frame.destroy()
    f2 = tk.Frame()
    f2.pack()
    f2.tkraise()
    lb1 = tk.Label(f2, width=50, text="Qual bar você vai frequentar?", font=fonte2).pack(padx=150, pady=10)
    bt1 = tk.Button(f2, width=25, text="Bela Dama", command=lambda:mostrar(f2, "Bella Dama", cardapio_bela_dama), font=fonte, bg="red").pack()
    bt2 = tk.Button(f2, width=25, text="Santo Pako", command=lambda:mostrar(f2, "Santo Pako", cardapio_santo_pako), font=fonte, bg="red").pack()
    bt3 = tk.Button(f2, width=25, text="Sujinhus", command=lambda:mostrar(f2, "Sujinhus", cardapio_sujinhus), font=fonte, bg="red").pack()
    lb3 = tk.Label(f2, text="").pack()
    lb2 = tk.Label(f2, text="Qual opção voce deseja acessar?", font=fonte2).pack()
    bt5 = tk.Button(f2, width=25, text="Ultimas Compras", command=lambda:Ultimas_compras(f2), font=fonte, bg="orange").pack()
    bt6 = tk.Button(f2, width=25, text="Informações Pessoais", command=lambda:informacoes_pessoais(f2), font=fonte, bg="orange").pack()

    
def informacoes_pessoais(frame):
    frame.destroy()
    f3 = tk.Frame()
    f3.pack()
    f3.tkraise()
    frase1 = tk.Label(f3, text="DADOS DO USUÁRIO")
    frase1.grid(row=2 , column=1)
    frase2 = tk.Label(f3, text="Nome de usuário")
    frase2.grid(row=3, column=0)
    frase3 = tk.Label(f3, text="Data de Nascimento")
    frase3.grid(row=4 , column=0)
    frase4 = tk.Label(f3, text="CPF")
    frase4.grid(row=5 , column=0)
    frase5 = tk.Label(f3, text="e-mail")
    frase5.grid(row=6 , column=0)
    frase6 = tk.Label(f3, text="ENDEREÇO DE COBRANÇA")
    frase6.grid(row=7 , column=1)
    frase7 = tk.Label(f3, text="Cidade")
    frase7.grid(row=8 , column=0)
    frase8 = tk.Label(f3, text="Rua")
    frase8.grid(row=9 , column=0)
    frase9 = tk.Label(f3, text="Complemento")
    frase9.grid(row=10 , column=0)
    frase11 = tk.Label(f3, text="Referência")
    frase11.grid(row=11 , column=0)
    frase12 = tk.Label(f3, text="DADOS DE PAGAMENTO")
    frase12.grid(row=12 , column=1)
    frase13 = tk.Label(f3, text="Nome (Como Impresso no Cartão)")
    frase13.grid(row=13 , column=0)
    frase14 = tk.Label(f3, text="Número do Cartão")
    frase14.grid(row=14 , column=0)
    frase15 = tk.Label(f3, text="Data de Vencimento")
    frase15.grid(row=15 , column=0)
    frase16 = tk.Label(f3, text="Código de Segurança")
    frase16.grid(row=16 , column=0)
    nome = tk.Label(f3, text=nome_final)
    nome.grid(row=3, column=1)
    nasc = tk.Label(f3, text=nasc_final)
    nasc.grid(row=4, column=1)
    cpf = tk.Label(f3, text=cpf_final)
    cpf.grid(row=5, column=1)
    mail = tk.Label(f3, text=mail_final)
    mail.grid(row=6, column=1)
    city = tk.Label(f3, text=city_final)
    city.grid(row=8, column=1)
    rua = tk.Label(f3, text=rua_final)
    rua.grid(row=9, column=1)
    cpl = tk.Label(f3, text=complemento_final)
    cpl.grid(row=10, column=1)
    ref = tk.Label(f3, text=ref_final)
    ref.grid(row=11, column=1)
    ncard = tk.Label(f3, text=ncard_final)
    ncard.grid(row=13, column=1)
    nume = tk.Label(f3, text=nume_final)
    nume.grid(row=14, column=1)
    venc = tk.Label(f3, text=venc_final)
    venc.grid(row=15, column=1)
    cod = tk.Label(f3, text=cod_final)
    cod.grid(row=16, column=1)          
    tk.Button(f3, text="Voltar Pagina Inicial", command=lambda:inicial3(f3), font=fonte, bg="grey").grid(row=20, column=1)
    
    
def criar_conta(frame):
    global nome
    global nasc
    global cpf
    global mail
    global city
    global rua
    global compl
    global ref
    global ref
    global ncard
    global nume
    global venc
    global code
    global senha1
    frame.destroy()
    f3 = tk.Frame()
    f3.pack()
    f3.tkraise()
    tk.Label(f3, text="Criar Conta", font=fonte2).grid(row=0, column=0)
    nome=tk.Entry(f3)
    nome.grid(row=3, column=1)
    nasc=tk.Entry(f3)
    nasc.grid(row=4, column=1)
    cpf=tk.Entry(f3)
    cpf.grid(row=5, column=1)
    mail=tk.Entry(f3)
    mail.grid(row=6, column=1)
    city=tk.Entry(f3)
    city.grid(row=8, column=1)
    rua=tk.Entry(f3)
    rua.grid(row=9, column=1)
    compl=tk.Entry(f3)
    compl.grid(row=10, column=1)
    ref=tk.Entry(f3)
    ref.grid(row=11, column=1)
    ncard=tk.Entry(f3)
    ncard.grid(row=13, column=1)
    nume=tk.Entry(f3)
    nume.grid(row=14, column=1)
    venc=tk.Entry(f3)
    venc.grid(row=15, column=1)
    code=tk.Entry(f3)
    code.grid(row=16, column=1)
    senha1 = tk.Entry(f3, show="*")
    senha1.grid(row=18, column=1)
    senha2 = tk.Entry(f3, show="*")
    senha2.grid(row=19, column=1)
    frase1 = tk.Label(f3, text="DADOS DO USUÁRIO")
    frase1.grid(row=2 , column=1)
    frase2 = tk.Label(f3, text="Nome de usuário")
    frase2.grid(row=3, column=0)
    frase3 = tk.Label(f3, text="Data de Nascimento")
    frase3.grid(row=4 , column=0)
    frase4 = tk.Label(f3, text="CPF")
    frase4.grid(row=5 , column=0)
    frase5 = tk.Label(f3, text="e-mail")
    frase5.grid(row=6 , column=0)
    frase6 = tk.Label(f3, text="ENDEREÇO DE COBRANÇA")
    frase6.grid(row=7 , column=1)
    frase7 = tk.Label(f3, text="Cidade")
    frase7.grid(row=8 , column=0)
    frase8 = tk.Label(f3, text="Rua")
    frase8.grid(row=9 , column=0)
    frase9 = tk.Label(f3, text="Complemento")
    frase9.grid(row=10 , column=0)
    frase11 = tk.Label(f3, text="Referência")
    frase11.grid(row=11 , column=0)
    frase12 = tk.Label(f3, text="DADOS DE PAGAMENTO")
    frase12.grid(row=12 , column=1)
    frase13 = tk.Label(f3, text="Nome (Como Impresso no Cartão)")
    frase13.grid(row=13 , column=0)
    frase14 = tk.Label(f3, text="Número do Cartão")
    frase14.grid(row=14 , column=0)
    frase15 = tk.Label(f3, text="Data de Vencimento")
    frase15.grid(row=15 , column=0)
    frase16 = tk.Label(f3, text="Código de Segurança")
    frase16.grid(row=16 , column=0)
    frase17 = tk.Label(f3, text="SENHA")
    frase17.grid(row=17, column=1)
    frase18 = tk.Label(f3, text="digite a senha")
    frase18.grid(row=18, column=0)
    frase19 = tk.Label(f3, text="digite a senha novamente")
    frase19.grid(row=19, column=0)
    tk.Label(f3, text="").grid()
    tk.Button(f3, text="Aplicar", command=lambda:entrar(f3), font=fonte, bg="grey").grid()
    tk.Label(f3, text="").grid()
   

def Ultimas_compras(frame):
    frame.destroy()
    f4 = tk.Frame()
    f4.pack()
    f4.tkraise()
    tk.Label(f4, text="Ultimas Compras", font=fonte).pack()
    tk.Button(f4, text="Voltar Pagina Inicial", command=lambda:inicial3(f4), font=fonte, bg="grey").pack()
    
    
def entrar (frame):
    global nome_final
    global nasc_final
    global cpf_final
    global mail_final
    global city_final
    global rua_final
    global complemento_final
    global ref_final
    global ncard_final
    global nume_final
    global venc_final 
    global cod_final
    global usuario_final
    global senha_final
    global senha_final2
    global usuario
    global senha
    senha_final = senha1.get()
    nome_final = nome.get()
    nasc_final = nasc.get()
    cpf_final = cpf.get()
    mail_final = mail.get()
    city_final = city.get()
    rua_final = rua.get()
    complemento_final = compl.get() 
    ref_final = ref.get()
    ncard_final = ncard.get()
    nume_final = nume.get()
    venc_final = venc.get()
    cod_final = code.get()
    lista = [nome_final, senha_final]
    print(lista)
    frame.destroy()
    f1 = tk.Frame()
    f1.pack()
    f1.tkraise()
    tk.Label(f1, text="UBAR", font=fonte3, fg="red").grid(row=0, column=2)
    tk.Label(f1, text="nome:").grid(row=2, column=1)
    tk.Label(f1, text="senha:").grid(row=3, column=1)
    usuario = tk.Entry(f1)
    usuario.grid(row=2, column=2)
    senha = tk.Entry(f1, show="*")
    senha.grid(row=3, column=2)
    tk.Button(f1, text="entrar",  command=lambda:inicial(f1), font=fonte).grid(row=4, column=2)
    tk.Label(f1, text="ainda não é cadastrado?").grid(row=6, column=3)
    tk.Button(f1, text="clique aqui", command=lambda:criar_conta(f1)).grid(row=6, column=4)



cardapio_sujinhus = [["Skol Litão: R$9,00", 9],["Frangolone: R$6,00", 6],["Pastel: R$5,00", 5]]
cardapio_santo_pako = [["Torre de chopp: R$65,00", 65],["Sucão 5L: R$105,00", 105],["Batata Frita com Cheddar e Bacon R$27,00", 27]]
cardapio_bela_dama = [["Itaipava Litrão: R$7,00",7],["Provolone: R$34,00",34],["Polenta: R$19,00", 19]] 

fontep= ("Verdana", 8)
fonte10=("Verdana", 10)
fonte = ("Verdana", 12)
fonte3= ("Verdana", 20)
fonte2= ("Verdana", 16)


root = tk.Tk()
root.geometry('700x600')
root.title("Ubar")
root.iconbitmap('favicon.ico')


f1 = tk.Frame()
f1.pack()
f1.tkraise()
tk.Label(f1, text="UBAR", font=fonte3, fg="red").grid(row=0, column=2)
tk.Label(f1, text="nome:").grid(row=2, column=1)
tk.Entry(f1).grid(row=2, column=2)
tk.Label(f1, text="senha:").grid(row=3, column=1)
tk.Entry(f1, show="*").grid(row=3, column=2)
tk.Button(f1, text="entrar",  font=fonte).grid(row=4, column=2)
tk.Label(f1, text="ainda não é cadastrado?").grid(row=6, column=3)
tk.Button(f1, text="clique aqui", command=lambda:criar_conta(f1)).grid(row=6, column=4)
root.mainloop()
