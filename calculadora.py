from tkinter import *
import tkinter.font as tkfont

janela = Tk()
janela.title("Calculadora")

# Definindo a fonte com um tamanho maior
fonte = ("Arial", 25)
f = font=("Arial", 20)
f2 = font=("Arial", 18)

cor1 = "#38576b"
cor2 = "#d76f3b"
cor3 = "#ffffff"

def soma0():
    global amostra
    global amostraV
    amostraV += '0'
    amostra += '0'
    ap.config(text=amostraV)

def soma1():
    global amostra
    global amostraV
    amostraV += '1'
    amostra += '1'
    ap.config(text=amostraV)
 

def soma2():
    global amostra
    global amostraV
    amostraV += '2'
    amostra += '2'
    ap.config(text=amostraV)
 

def soma3():
    global amostra
    global amostraV
    amostraV += '3'
    amostra += '3'
    ap.config(text=amostraV)
 

def soma4():
    global amostra
    global amostraV
    amostraV += '4'
    amostra += '4'
    ap.config(text=amostraV)
 

def soma5():
    global amostra
    global amostraV
    amostraV += '5'
    amostra += '5'
    ap.config(text=amostraV)
 

def soma6():
    global amostra
    global amostraV
    amostraV += '6'
    amostra += '6'
    ap.config(text=amostraV)
 

def soma7():
    global amostra
    global amostraV
    amostraV += '7'
    amostra += '7'
    ap.config(text=amostraV)
 

def soma8():
    global amostra
    global amostraV
    amostraV += '8'
    amostra += '8'
    ap.config(text=amostraV)
 

def soma9():
    global amostra
    global amostraV
    amostraV += '9'
    amostra += '9'
    ap.config(text=amostraV)

def clear():
    global amostra
    global amostraV
    global conj
    global Sw
    global Aw
    global sem_con
    amostraV = ""
    amostra = ""
    conj = []
    Sw = 0
    Aw = 0
    sem_con = 0
    ap.config(text=amostraV)


def ereaze():
    global amostra
    global amostraV
    a = list(amostraV)
    a.pop()
    amostraV = "".join(a)
    amostra = "".join(a)
    ap.config(text=amostraV)

def Nsei():
    global amostra
    global amostraV
    conj.append(amostra)
    amostraV = ""
    amostra = ""
    ap.config(text=amostraV)

def Ba():
    global amostra
    Nsei()
    amostra += '+'


def Bs():
    global amostra
    Nsei()
    amostra += '-'

def Bd():
    global amostra
    Nsei()
    amostra += '/'

def Bv():
    global amostra
    Nsei()
    amostra += 'x'


def Br():
    global amostra
    amostra += 'r'
    Nsei()
    
def bença(a):
    a = 0
    return a

def reposta():
    global amostra
    global amostraV
    global conj
    global Sw
    global Aw
    global sem_con
    global resp
    Aw = 0
    Sw = 0
    conj.append(amostra)
    for e, i in enumerate(conj):
        if "+" in i:
            n = i.replace('+', '')
            print('\nvolers de n: ', n, '\n')
            n = float(n)
            Aw += n
        elif "-" in i:
            n = i.replace('-', '')
            n = float(n)
            Sw += n
        elif "/" in i:
            n = i.replace('/', '')
            n = float(n)
            a = conj[e - 1]
            a = float(a)
            Aw = Aw - a
            n = a/n
            if n < 0:
                Sw += n
            else:
                Aw += n
        elif "x" in i:
            n = i.replace('x', '')
            n = float(n)
            a = conj[e - 1]
            a = float(a)
            Aw = Aw - a
            n = a*n
            if n < 0:
                Sw += n
            else:
                Aw += n
        elif "r" in i:
            n = i.replace('r', '')
            n = float(n)
            n = n ** 0.5
            if n < 0:
                Sw += n
            else:
                Aw += n
        else:
            r = i
            if i == "":
              r = 0 
            r = float(r)
            sem_con = r

    resp = sem_con + Aw - Sw

    print(sem_con, "sem sinal")
    print(Aw, "soma")
    print(Sw, "subtração")
    print(resp, "é a resposta final\n")

    amostra = str(resp)
    amostraV = str(resp)
    amostraV = float(amostraV)
    if amostraV.is_integer():
        amostraV = int(amostraV)


    amostraV = str(amostraV)

    ap.config(text=amostraV)
    conj = []

amostra = ""
amostraV = ""
conj = []
Sw = 0
Aw = 0
sem_con = 0
resp = 0



ap = Label(janela, text=amostraV, fg=cor3, height=4, width=23, font=fonte, bg=cor1)
ap.grid(column=1, columnspan=4, row=1)

B1 = Button(janela, text="1", font=fonte, command=soma1, width=5, height=2)
B1.grid(column=1, row=3, sticky="nsew")

B2 = Button(janela, text="2", font=fonte, command=soma2, width=5, height=2)
B2.grid(column=2, row=3, sticky="nsew")

B3 = Button(janela, text="3", font=fonte, command=soma3, width=5, height=2)
B3.grid(column=3, row=3, sticky="nsew")

B4 = Button(janela, text="4", font=fonte, command=soma4, width=5, height=2)
B4.grid(column=1, row=4, sticky="nsew")

B5 = Button(janela, text="5", font=fonte, command=soma5, width=5, height=2)
B5.grid(column=2, row=4, sticky="nsew")

B6 = Button(janela, text="6", font=fonte, command=soma6, width=5, height=2)
B6.grid(column=3, row=4, sticky="nsew")

B7 = Button(janela, text="7", font=fonte, command=soma7, width=5, height=2)
B7.grid(column=1, row=5, sticky="nsew")

B8 = Button(janela, text="8", font=fonte, command=soma8, width=5, height=2)
B8.grid(column=2, row=5, sticky="nsew")

B9 = Button(janela, text="9", font=fonte, command=soma9, width=5, height=2)
B9.grid(column=3, row=5, sticky="nsew")

B0 = Button(janela, text="0", font=fonte, command=soma0, width=11, height=2)
B0.grid(column=1, columnspan=2, row=6, sticky="nsew")

Bp = Button(janela, text=".", font=fonte, width=5, height=2)
Bp.grid(column=3, row=6, sticky="nsew")

Bi = Button(janela, text="=", font=fonte, bg=cor1, activebackground=cor1, fg=cor3, width=5, height=2, command=reposta)
Bi.grid(column=3, row=6, sticky="nsew")

Bapp = Button(janela, text="√", font=f, width=6, height=2, command=Br)
Bapp.grid(column=4, row=2, sticky="nsew")

BDi = Button(janela, text="/", font=fonte, width=5, height=2, command=Bd)
BDi.grid(column=4, row=3, sticky="nsew")

BVe = Button(janela, text="*", font=fonte, width=5, height=2, command=Bv)
BVe.grid(column=4, row=4, sticky="nsew")

Bm = Button(janela, text="-", font=fonte, width=5, height=2, command=Bs)
Bm.grid(column=4, row=5, sticky="nsew")

BM = Button(janela, text="+", font=fonte, width=5, height=2, command=Ba)
BM.grid(column=4, row=6, sticky="nsew")

Bap = Button(janela, text="C", font=f, bg=cor2, activebackground=cor2, width=13, height=2, command=clear)
Bap.grid(column=1,columnspan=2, row=2, sticky="nsew")

Bapn = Button(janela, text="CE", font=f, width=6, height=2, command=ereaze)
Bapn.grid(column=3, row=2, sticky="nsew")


janela.mainloop()