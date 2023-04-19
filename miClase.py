#aqui estaran las funciones de la base de datos 

from tkinter import messagebox
import sqlite3

class FuncionesBD:
    def __init__(self):
        self.__BaseDatos = 'BDExportaciones.db'
        
    def __conectaBD(self):
        try:
            Conexion = sqlite3.connect(self.__BaseDatos)
            return Conexion
        except sqlite3.OperationalError:    
            messagebox.showerror("Error!","Error al conectar a la base de datos")
    
    def insertaPedimento(self,Transporte,Aduana):
        #comprobamos que no haya campos vacios
        if(Transporte=="" or Aduana==""):
            messagebox.showwarning("Aviso!","Completa TODOS los campos")
            return
        try:
            Conexion = self.__conectaBD()
            Cursor = Conexion.cursor()   
            Datos = [Transporte,Aduana]
            SQL = "INSERT INTO TBPedimentos(Transporte,Aduana)VALUES(?,?)"
            Cursor.execute(SQL,Datos)    
            Conexion.commit()
            Conexion.close()
            messagebox.showinfo("Exito","Se inserto correctamente") 
        except sqlite3.OperationalError as e:    
            messagebox.showerror("Error!","Ha ocurrido un error:"+str(e))