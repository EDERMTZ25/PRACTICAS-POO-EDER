from tkinter import*
from tkinter import ttk
import tkinter as tk 

Ventana= Tk()
Ventana.title("UsuariosCRUD")
Ventana.geometry("500X300")
panel=ttk.Notebook(Ventana)
panel.pack(fill="booth", expand= "yes")

pestana1= ttk.Frame(panel)
pestana2= ttk.Frame(panel)
pestana3= ttk.Frame(panel)
pestana4= ttk.Frame(panel)

#PESTAÑA 1 FORMULARIO USUARIOS

titulo= Label(pestana1, text= "REGISTRO USUARIOS", fg="blue", front=("Modern", 18)).pack()

varNom=tk.StringVar()
lblNom= Label(pestana1, text="Nombre").pack()
txtNom= Entry(pestana1, textvariable=varNom).pack()

varCor=tk.StringVar()
lblCor= Label(pestana1, text="Correo").pack()
txtCor= Entry(pestana1, textvariable=varCor).pack()

varCon=tk.StringVar()
lblCon= Label(pestana1, text="Contraseña").pack()
txtCon= Entry(pestana1, textvariable=varCon).pack()

btnGuardar= Button(pestana1, text="GUARDAR USUARIO").pack()

panel.add(pestana1, text="FORMULARIO USUARIOS")
panel.add(pestana2, text= "BUSCAR USUARIOS")
panel.add(pestana3, text= "CONSULTAR USUARIOS")
panel.add(pestana4, text= "ACTUALIZAR USUARIOS")

Ventana.mainloop()