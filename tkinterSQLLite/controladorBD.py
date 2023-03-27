from tkinter import messagebox
import sqlite3 
import bcrypt

class controladorBD:
    
    def __init__(self):
        pass
    
    # se realizo la coneccion para usarla cuando sea necesario
    def conexionBD(self):
        
        try:
            conexion= sqlite3.connect("C:\UsersHP\Documents\GitHub\PRACTICAS-POO-EDER\tkinterSQLLite\TBagregados.db")
            print("conectado a la base de datos")
            return conexion
        
        except sqlite3.OperationalError:
            print("No se pudo conectar") 



    # Metodo para insertar        
    def gardarUsuario(self,nom,cor,con):
        
        #1.- llamar a la conexion
        conx= self.conexionBD()
        
        #2.- revisar que los parametros no estan vacios
        if(nom == "" or cor == "" or con == ""):
            messagebox.showwarning("cuidadito!!", "falta informacion")
            conx.close()
        else:
            #3.- prepara datos y el querySQL
            cursor= conx.cursor()
            conH=self.encriptarCon(con)
            datos=(nom,cor,conH)
            qrinsert="insert into TBagregados(Nombre,Correo,Contra) values(?,?,?)"
            
            #4.- proceder a insertar y cerramos conexion
            cursor.execute(qrinsert,datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito"," Se guardo el usuario")
            
    def encriptarCon(self,con):
        conflat= con
        conflat= conflat.encode() #convertirno con a bytes
        sal = bcrypt.gensalt()
        conHa= bcrypt.hashpw(conflat,sal)
        print(conHa)
        return conHa
