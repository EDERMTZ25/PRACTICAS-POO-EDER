from tkinter import *
from tkinter.ttk import *

index=Tk()
index.title("LOGIN")
index.geometry("300x150")
index.resizable(width=False, height=False)

luser=Label(index, text="Ingrese nombre de usuario:")
luser.pack()

user=StringVar()
euser=Entry(index, width=30, textvariable=user)
euser.pack()

lpas=Label(index, text="Password:")
lpas.pack()

pas=StringVar()
epas=Entry(index, width=30, textvariable=pas, show="*")
epas.pack()

def ingresar():
    if user.get()=="python" and pas.get()=="12345":
        Message.title("Correcto")

    else:
        Message.title("Incorrecto")

b1=Button(index, text="Entrar", command=ingresar)
b1.pack(side=BOTTOM)

index.mainloop()