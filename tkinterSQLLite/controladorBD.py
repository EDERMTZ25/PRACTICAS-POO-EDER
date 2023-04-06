import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import bcrypt


class ControladorBD:
    def __init__(self):
        pass

    def conexionBD(self):
        try:
            conexion = sqlite3.connect("usuarios_bd.db")
        # print("Conectado con exito")
            return conexion
        except sqlite3.OperationalError:
            print("Fallo en la conexion")

    def encriptarContra(self, contra):
        # Encritar contraseña con bcrypt
        contraPlana = contra
        contraPlana = contraPlana.encode()  # Convertir contraseña a Bytes
        sal = bcrypt.gensalt()
        contraEncriptada = bcrypt.hashpw(contraPlana, sal)
        return contraEncriptada

    def guardarUsuario(self, nombre, correo, contra):
        conx = self.conexionBD()

        if (nombre == "" or correo == "" or contra == ""):
            messagebox.showwarning("CUIDADO", "Revisa tus datos, uno o mas campos estan vacios")
            conx.close()
            return
        elif (nombre == "" and correo == "" and contra == ""):
            messagebox.showwarning("CUIDADO", "Todos los campos estan vacios")
            conx.close()
            return
        else:
            cursor = conx.cursor()
            conH = self.encriptarContra(contra)
            datos = (nombre, correo, conH)
            consulta = "insert into TBRegistros(nombre, correo, contra) values(?,?,?)"
            # print(nombre, correo, contra)
            cursor.execute(consulta, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("EXITO", "Se guardo el usuario")

    def consultarUsuario(self, id):
        # Buscar usuario en la base de datos por su id
        conx = self.conexionBD()
        cursor = conx.cursor()
        try:
            cursor.execute("select * from TBRegistros where id = ?", (id,))
            usuario = cursor.fetchall()
            conx.close()

            # Comprobar si el usuario existe
            if len(usuario) == 0:
                # Si el usuario no existe se retorna None y se muestra un mensaje de error
                messagebox.showwarning("Error", "El usuario no existe")
                return None
            else:
                # Si el usuario existe se retorna el usuario encontrado
                return usuario
        # Si ocurre un error al consultar el usuario se muestra un mensaje de error
        except sqlite3.OperationalError:
            messagebox.showwarning("Error", "Ocurrio un error al consultar el usuario")

    def consultarTodos(self):
        # Buscar usuario en la base de datos por su id
        conx = self.conexionBD()
        cursor = conx.cursor()
        try:
            cursor.execute("select id, nombre, correo from TBRegistros")
            usuario = cursor.fetchall()
            conx.close()

            # Comprobar si el usuario existe
            if len(usuario) == 0:
                # Si el usuario no existe se retorna None y se muestra un mensaje de error
                messagebox.showwarning("Error", "La tabla no existe o esta vacia")
                return None
            else:
                # Si el usuario existe se retorna el usuario encontrado
                return usuario
        # Si ocurre un error al consultar el usuario se muestra un mensaje de error
        except sqlite3.OperationalError:
            messagebox.showwarning("Error", "Ocurrio un error al consultar la tabla")

    def actualizarUsuario(self, id, nombre, correo, contra):
        # Buscar usuario en la base de datos por su id y actualizarlo
        if (id == "" and correo == "" and contra == "" and nombre == ""):
            messagebox.showwarning("CUIDADO", "Todos los campos estan vacios")
            return
        elif (id == "" or correo == "" or contra == "" or nombre == ""):
            messagebox.showwarning("CUIDADO", "Revisa tus datos, uno o mas campos estan vacios")
            return

        #Validar que el id sea un numero
        try:
            id = int(id)
        except ValueError:
            messagebox.showwarning("CUIDADO", "El id debe ser un numero")
            return

        conx = self.conexionBD()
        cursor = conx.cursor()

        #Validar que el id exista
        cursor.execute("select * from TBRegistros where id = ?", (id,))
        usuario = cursor.fetchall()
        if len(usuario) == 0:
            messagebox.showwarning("CUIDADO", "El id no existe")
            return
        # Si el usuario existe se intenta actualizar
        try:
            # Encriptar contraseña
            contra = self.encriptarContra(contra)
            cursor.execute("UPDATE TBRegistros SET nombre = ?, correo = ?, contra = ? WHERE id = ?", (nombre, correo, contra, id))
            conx.commit()
            conx.close()
            messagebox.showinfo("EXITO", "Se actualizo el usuario")
        # Si ocurre un error al consultar el usuario se muestra un mensaje de error
        except sqlite3.OperationalError:
            messagebox.showwarning("Error", "Ocurrio un error al actualizar el usuario")

    def eliminarUsuario(self, id):
        # Buscar usuario en la base de datos por su id y eliminarlo
        if (id == ""):
            messagebox.showwarning("CUIDADO", "El campo id esta vacio")
            return

        #Validar que el id sea un numero
        try:
            id = int(id)
        except ValueError:
            messagebox.showwarning("CUIDADO", "El id debe ser un numero")
            return

        conx = self.conexionBD()
        cursor = conx.cursor()

        #Validar que el id exista
        cursor.execute("select * from TBRegistros where id = ?", (id,))
        usuario = cursor.fetchall()
        if len(usuario) == 0:
            messagebox.showwarning("CUIDADO", "El id no existe")
            return
        # Si el usuario existe se intenta eliminar
        try:
            cursor.execute("DELETE FROM TBRegistros WHERE id = ?", (id,))
            conx.commit()
            conx.close()
            messagebox.showinfo("EXITO", "Se elimino el usuario")
        # Si ocurre un error al consultar el usuario se muestra un mensaje de error
        except sqlite3.OperationalError:
            messagebox.showwarning("Error", "Ocurrio un error al eliminar el usuario")


