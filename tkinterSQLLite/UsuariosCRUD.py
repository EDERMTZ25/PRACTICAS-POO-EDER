from tkinter import*
from tkinter import ttk
import tkinter as tk
from controladorBD import*
from tkinter import messagebox

#crear un objeto tipo controlador
controlador= controladorBD()

#proceder a guadar el metodo guardarUsuario() del objeto controlador
def ejecutarInsert():
    controlador.guardarUsuario(varNom.get(),varCor.get(),varCon())


def ejecutaSelectU():
    rsUsuario=controlador.consultarUsuario(varbus.get())
    for usu in rsUsuario:
        cadena=str(usu[0])+" "+ usu[1]+ " "+ usu[2]+ " "+ str(usu[3])
        
    if(rsUsuario):
        print(cadena)
    else:
        messagebox.showinfo("Usuario no registrado en la base de datos")



ventana = Tk()
ventana.title("CRUD Usuarios")
ventana.geometry("500x300")

panel= ttk.Notebook(ventana)
panel.pack(fill="both", expand="yes")

pestana1=ttk.Frame(panel)
pestana2=ttk.Frame(panel)
pestana3=ttk.Frame(panel)
pestana4=ttk.Frame(panel)

#pestaña 1
titulo= Label(pestana1, text="Resgistrp de Usurios", fg="blue", font=("Modern",18) ).pack()
varNom= tk.StringVar()
lblNom= Label(pestana1, text="nombre: ").pack()
txtNom= Entry(pestana1, textvariable=varNom ).pack()

varCor= tk.StringVar()
lblCor= Label(pestana1, text="correo: ").pack()
txtcor= Entry(pestana1, textvariable=varCor ).pack()

varCon= tk.StringVar()
lblCon= Label(pestana1, text="contraseña: ").pack()
txtcon= Entry(pestana1, textvariable=varCon ).pack()

btnGuardar= Button(pestana1, text="Guardar Usuario").pack()


#pestaña 2 Buscar Usuario
titulo2= Label(pestana2, text="Buscar Usurios", fg="green", font=("Modern",18) ).pack()

varbus= tk.StringVar()
lblid= Label(pestana2, text="Identificador de usuario: ").pack()
txtid= Entry(pestana2, textvariable=varbus ).pack()
btnBusqueda= Button(pestana2, text="Buscar",command=ejecutaSelectU).pack()

subBus= Label(pestana2,text="Registrado: ",fg="blue",font=("Modern",15)).pack()
texBus=tk.Text(pestana2,height=5,width=52).pack()








panel.add(pestana1, text="Formulario de Usuarios")
panel.add(pestana2, text="Buscar Usuarios")
panel.add(pestana3, text="Consultar Usuario")
panel.add(pestana4, text="Actualiar Usuario")





ventana.mainloop()