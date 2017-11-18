from sqlite3 import *
from time import *
import os
import msvcrt

from functools import partial

db = connect('clientes.db')
cursor = db.cursor()

def ct():


    cursor.execute("DROP TABLE IF EXISTS clientes")
    db.commit()

    cursor.execute("""
    CREATE TABLE clientes(
        nome TEXT NOT NULL,
        idade TEXT,
        sexo VARCHAR(1) NOT NULL,
        identidade TEXT NOT NULL,
        cpf VARCHAR(11) NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT,
        endereco TEXT,
        plano TEXT,
        tratamento TEXT,
        complemento TEXT,
        criado_em DATE NOT NULL
    );
    """)
    print("TABELA CRIADA COM SUCESSO!")



def inserir():

    import os
    import msvcrt

    import time

    str(e1.get())

    a = str(e1.get())
    b = str(e2.get())
    c = str(e3.get())
    d = str(e4.get())
    e = str(e5.get())
    f = str(e6.get())
    g = str(e7.get())
    h = str(e8.get())
    i = str(e9.get())
    j = str(e10.get())
    k = str(e11.get())
    dt = str(time.strftime('%d/%m/%Y'))

    cursor.execute('INSERT INTO clientes VALUES (?,?,?,?,?,?,?,?,?,?,?,?)', (a,b,c,d,e,f,g,h,i,j,k,dt))
    db.commit()

    db.close()

    print()
    print('CLIENTE CADASTRADO COM SUCESSO')
    # press = msvcrt.getch()
    # clear = os.system('cls')



from tkinter import *

ct()

w = Tk()
w.geometry("500x500")
w.title("Gerenciamento")

bt = Button(w, text="Salvar", command=inserir)

# s['command'] = partial(inserir, )

e1 = Entry(w)
e2 = Entry(w)
e3 = Entry(w)
e4 = Entry(w)
e5 = Entry(w)
e6 = Entry(w)
e7 = Entry(w)
e8 = Entry(w)
e9 = Entry(w)
e10 = Entry(w)
e11 = Entry(w)

# a = str(e1.get())
# b = int(e2.get())
# c = str(e3.get())
# d = int(e4.get())
# e = str(e5.get())
# f = str(e6.get())
# g = str(e7.get())
# h = str(e8.get())
# i = str(e9.get())
# j = str(e10.get())
# k = str(e11.get())

l1 = Label(w, text="Nome:")
l2 = Label(w, text="Idade:")
l3 = Label(w, text="Sexo:")
l4 = Label(w, text="Identidade:")
l5 = Label(w, text="CPF:")
l6 = Label(w, text="Email:")
l7 = Label(w, text="Telefone:")
l8 = Label(w, text="Endereço:")
l9 = Label(w, text="Plano de Saúde:")
l10 = Label(w, text="Tratamento:")
l11 = Label(w, text="Complemento:")


l1.pack(side=TOP, fil=BOTH)
e1.pack(side=TOP, fil=BOTH)
l2.pack(side=TOP, fil=BOTH)
e2.pack(side=TOP, fil=BOTH)
l3.pack(side=TOP, fil=BOTH)
e3.pack(side=TOP, fil=BOTH)
l4.pack(side=TOP, fil=BOTH)
e4.pack(side=TOP, fil=BOTH)
l5.pack(side=TOP, fil=BOTH)
e5.pack(side=TOP, fil=BOTH)
l6.pack(side=TOP, fil=BOTH)
e6.pack(side=TOP, fil=BOTH)
l7.pack(side=TOP, fil=BOTH)
e7.pack(side=TOP, fil=BOTH)
l8.pack(side=TOP, fil=BOTH)
e8.pack(side=TOP, fil=BOTH)
l9.pack(side=TOP, fil=BOTH)
e9.pack(side=TOP, fil=BOTH)
l10.pack(side=TOP, fil=BOTH)
e10.pack(side=TOP, fil=BOTH)
l11.pack(side=TOP, fil=BOTH)
e11.pack(side=TOP, fil=BOTH)

bt.pack(side=BOTTOM, fil=BOTH)




w.mainloop()