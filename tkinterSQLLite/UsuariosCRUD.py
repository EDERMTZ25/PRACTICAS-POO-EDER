import tkinter as tk
from tkinter import ttk, END
from tkinter import messagebox
from ControladorBD import *

#. Crear una objeto de tipo contralador
controlador= ControladorBD()

#Procedermos a guardar usando el metodo del objeto controlador.
def ejecutaInsert():
    controlador.guardarUsuario(varNombre.get(),varCorreo.get(),varContra.get())


# Funcion para buscar a un usuario con id y ponerlo en el cuadro de text
def buscar():
    busqueda = controlador.consultarUsuario(varId.get())
    txtMostrar.delete('0.0',END)

    # Damos formato a la busqueda para mostrarla en el cuadro de texto (Solo se muestra el id, nombre y correo)
    if busqueda != None:
        for usu in busqueda:
            cadena2 = (" | ID: " + str(usu[0]) + " | Nombre: " + usu[1] + " | Correo: " + usu[2] + " | ")

        txtMostrar.insert('0.0', cadena2)
    else:
        pass




# Funcion para traer todos los usuarios
def mostrar_todos():
    #Borrar datos del treeview anterior
    tree.delete(*tree.get_children())

    # Agregar todos los usuarios a un treeview
    rsUsuarios = controlador.consultarTodos()

    #Valida que haya datos en la variable rsUsuarios
    if rsUsuarios != None:
        for usu2 in rsUsuarios:
            tree.insert(parent='',index='end',values=(usu2[0],usu2[1],usu2[2]))
    else:
        pass

# Funcion para actualizar un usuario
def actualizar():
    controlador.actualizarUsuario(varId_actu.get(), varNombre_actu.get(), varCorreo_actu.get(), varContra_actu.get())

# Funcion para eliminar un usuario
def eliminar():
    if varConfirmar.get() == 1:
        controlador.eliminarUsuario(varId_elim.get())
        # Limpiar el campo de texto de eliminar usuario y el checkbutton
        varConfirmar.set(0)
        varId_elim.set("")
    else:
        messagebox.showwarning("CUIDADO", "Debe confirmar la eliminacion")


# Funcion para limpiar los campos de texto de ingresar usuario y actualizar usuario
def limpiar_ingresar():
    varNombre.set("")
    varCorreo.set("")
    varContra.set("")


def limpiar_actualizar():
    varId_actu.set("")
    varNombre_actu.set("")
    varCorreo_actu.set("")
    varContra_actu.set("")

#Creacion de la ventana principal (CRUD)

Ventana = tk.Tk()
Ventana.title("CRUD")
Ventana.geometry("800x600")

#Creacion de las pestañas
#Panel de pestañas Notebook
panel = ttk.Notebook(Ventana)
panel.pack(fill="both", expand="yes")

#Creacion de las pestañas
#Pestaña 1
pestana1 = ttk.Frame(panel)
panel.add(pestana1, text="Ingresar Usuario")

# Agregar los widgets a la pestaña de ingresar usuario y darle formato
titulo_p1 = tk.Label(pestana1, text="Ingresar Usuario", fg="green", font=("Arial", 20)).pack()

# Crear los campos de texto para ingresar usuario
nombre = tk.Label(pestana1, text="Nombre: ", font=("Arial", 12)).pack(padx=10, pady=10)
varNombre = tk.StringVar() #Variable para guardar el nombre
txtNombre = tk.Entry(pestana1, textvariable=varNombre, font=("Arial", 12)).pack(padx=5, pady=5)


correo = tk.Label(pestana1, text="Correo: ", font=("Arial", 12)).pack(padx=10, pady=10)
varCorreo = tk.StringVar() #Variable para guardar el correo
txtCorreo = tk.Entry(pestana1, textvariable=varCorreo, font=("Arial", 12)).pack(padx=5, pady=5)

contra = tk.Label(pestana1, text="Contraseña: ", font=("Arial", 12)).pack(padx=10, pady=10)
varContra = tk.StringVar() #Variable para guardar la contraseña
txtContra = tk.Entry(pestana1, textvariable=varContra, font=("Arial", 12)).pack(padx=5, pady=5)

# Crear el boton para ingresar usuario y darle formato
btnIngresar = tk.Button(pestana1, text="Registrar usuario", font=("Arial", 12), bg="#18BBBB", fg="white", command=ejecutaInsert).pack(padx=10, pady=10)

# Crear el boton para limpiar los campos de texto
btnLimpiar = tk.Button(pestana1, text="Limpiar campos", font=("Arial", 12), bg="#16BF72", fg="white", command=limpiar_ingresar).pack(padx=10, pady=10)


#Pestaña 2
pestana2 = ttk.Frame(panel)
panel.add(pestana2, text="Buscar Usuario")

# Agregar los widgets a la pestaña de buscar usuario y darle formato
titulo_p2 = tk.Label(pestana2, text="Buscar Usuario", fg="blue", font=("Arial", 20)).pack()

# Crear los campos de texto para buscar usuario
id = tk.Label(pestana2, text="ID: ", font=("Arial", 12)).pack(padx=10, pady=10)
varId = tk.StringVar() #Variable para guardar el id
txtId = tk.Entry(pestana2, textvariable=varId, font=("Arial", 12)).pack(padx=5, pady=5)

# Crear el boton para buscar usuario y darle formato
btnBuscar = tk.Button(pestana2, text="Buscar usuario", font=("Arial", 12), bg="#18BBBB", fg="white", command=buscar).pack(padx=10, pady=10)

#Agregar un Textbox para mostrar los datos del usuario
titulo_texto = tk.Label(pestana2, text="Datos del usuario", font=("Arial", 12)).pack(padx=10, pady=10)
txtMostrar = tk.Text(pestana2, width=50, height=10, font=("Arial", 12))
txtMostrar.pack(padx=10, pady=10)



#Pestaña 3
pestana3 = ttk.Frame(panel)
panel.add(pestana3, text="Mostar Todos")

# Agregar los widgets a la pestaña de mostrar todos los usuarios y darle formato
titulo_p3 = tk.Label(pestana3, text="Mostrar Todos", fg="#14A6DC", font=("Arial", 20)).pack()

# Crear el boton para mostrar todos los usuarios y darle formato
btnMostrar = tk.Button(pestana3, text="Mostrar todos", font=("Arial", 12), bg="#18BBBB", fg="white", command=mostrar_todos).pack(padx=10, pady=10)

# Usar un Treeview para mostrar todos los usuarios
titulo_tree = tk.Label(pestana3, text="Todos los usuarios", font=("Arial", 12)).pack(padx=10, pady=10)
tree = ttk.Treeview(pestana3, columns=(1,2,3), show="headings", height="6")
tree.pack(padx=10, pady=10)
tree.heading(1, text="ID")
tree.heading(2, text="Nombre")
tree.heading(3, text="Correo")

tree.pack(padx=10, pady=10)


#Pestaña 4
pestana4 = ttk.Frame(panel)
panel.add(pestana4, text="Actualizar Usuario")

# Agregar los widgets a la pestaña de actualizar usuario y darle formato
titulo_p4 = tk.Label(pestana4, text="Actualizar Usuario", fg="#F19510", font=("Arial", 20)).pack()

# Crear los campos de texto para actualizar usuario
id = tk.Label(pestana4, text="ID: ", font=("Arial", 12)).pack(padx=10, pady=10)
varId_actu = tk.StringVar() #Variable para guardar el id
txtId_actu = tk.Entry(pestana4, textvariable=varId_actu, font=("Arial", 12)).pack(padx=5, pady=5)

nombre_actu = tk.Label(pestana4, text="Nombre: ", font=("Arial", 12)).pack(padx=10, pady=10)
varNombre_actu = tk.StringVar() #Variable para guardar el nombre
txtNombre_actu = tk.Entry(pestana4, textvariable=varNombre_actu, font=("Arial", 12)).pack(padx=5, pady=5)

correo_actu = tk.Label(pestana4, text="Correo: ", font=("Arial", 12)).pack(padx=10, pady=10)
varCorreo_actu = tk.StringVar() #Variable para guardar el correo
txtCorreo_actu = tk.Entry(pestana4, textvariable=varCorreo_actu, font=("Arial", 12)).pack(padx=5, pady=5)

contra_actu = tk.Label(pestana4, text="Contraseña nueva: ", font=("Arial", 12)).pack(padx=10, pady=10)
varContra_actu = tk.StringVar() #Variable para guardar la contraseña
txtContra_actu = tk.Entry(pestana4, textvariable=varContra_actu, font=("Arial", 12)).pack(padx=5, pady=5)

# Crear el boton para actualizar usuario y darle formato
btnActualizar = tk.Button(pestana4, text="Actualizar usuario", font=("Arial", 12), bg="#18BBBB", fg="white", command=actualizar).pack(padx=10, pady=10)

# Crear el boton para limpiar los campos de texto
btnLimpiar_actu = tk.Button(pestana4, text="Limpiar campos", font=("Arial", 12), bg="#16BF72", fg="white", command=limpiar_actualizar).pack(padx=10, pady=10)


#Pestaña 5
pestana5 = ttk.Frame(panel)
panel.add(pestana5, text="Eliminar Usuario")

# Agregar los widgets a la pestaña de eliminar usuario y darle formato
titulo_p5 = tk.Label(pestana5, text="Eliminar Usuario", fg="red", font=("Arial", 20)).pack()

# Crear los campos de texto para eliminar usuario
id = tk.Label(pestana5, text="ID: ", font=("Arial", 12)).pack(padx=10, pady=10)
varId_elim = tk.StringVar() #Variable para guardar el id
txtId_elim = tk.Entry(pestana5, textvariable=varId_elim, font=("Arial", 12)).pack(padx=5, pady=5)

# Agregar un checkbox para confirmar la eliminacion
varConfirmar = tk.IntVar()
confirmar = tk.Checkbutton(pestana5, text="Confirmar", variable=varConfirmar, font=("Arial", 12)).pack(padx=10, pady=10)

# Crear el boton para eliminar usuario y darle formato
btnEliminar = tk.Button(pestana5, text="Eliminar usuario", font=("Arial", 12), bg="red", fg="white", command=eliminar).pack(padx=10, pady=10)


#Ejecucion de la ventana
Ventana.mainloop()


