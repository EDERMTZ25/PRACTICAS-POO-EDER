from tkinter import *
from tkinter import ttk
import tkinter as tk
from controlBD import *

# crear una istancia de tipo controlador
controlador= controladorBD()

#Proseder a guardar usuario 
def ejecutarInsert():
    controlador.gardarUsuario(varNom.get(),varCor.get(),varPas.get())


ventana = Tk()
ventana.geometry("500x300")
ventana.title("CRUD Usuarios")

panel= ttk.Notebook(ventana)
panel.pack(fill="both",expand="yes")

blink1= ttk.Frame(panel)
blink2= ttk.Frame(panel)
blink3= ttk.Frame(panel)
blink4= ttk.Frame(panel)
#pestaña1: Formulario
titulo= Label(blink1,text="Registro Usuarios",fg="blue",font=("Modern",18)).pack()

varNom= tk.StringVar()
lblNom= Label(blink1,text="nombre:").pack()
txtNom= Entry(blink1,textvariable=varNom).pack()

varCor= tk.StringVar()
lblCor= Label(blink1,text="correo:").pack()
txtCor= Entry(blink1,textvariable=varCor).pack()

varPas= tk.StringVar()
lblPas= Label(blink1,text="contraseña:").pack()
txtPas= Entry(blink1,textvariable=varPas).pack()

btnGuard= Button(blink1,text="Guardar Usuario",command=ejecutarInsert).pack()

#pestaña2: Formulario
#pestaña3: Formulario
#pestaña4: Formulario





panel.add(blink1,text="formulario de usuarios")
panel.add(blink2,text="Agregar usuario")
panel.add(blink3,text="Consultar usuarios")
panel.add(blink4,text="Actualizar usuarios")

ventana.mainloop()