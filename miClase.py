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
            
    def consultaPedimento(self,Aduana):
        Conexion = self.__conectaBD()
        try:
            Cursor = Conexion.cursor()
            Datos = [Aduana]
            SQL = "SELECT * FROM TBPedimentos WHERE Aduana = ?"
            Cursor.execute(SQL,Datos) #Lanzamos la consulta
            ResultadosCons = Cursor.fetchall() #Guardamos los resultados de la consulta
            Conexion.close()
            return ResultadosCons 
        except sqlite3.OperationalError as e:
            messagebox.showerror("Error!","Ha ocurrido un error:"+str(e))      
            
    def eliminaPedimento(self,ID):
        Conexion = self.__conectaBD()
        try:
            Cursor = Conexion.cursor()
            Datos = [ID]
            SQL = "DELETE FROM TBPedimentos WHERE IDExpo = ?"
            Cursor.execute(SQL,Datos) #Lanzamos la consulta
            Conexion.commit()
            Conexion.close()
            messagebox.showinfo("Exito","Se Elimino correctamente") 
        except sqlite3.OperationalError as e:
            messagebox.showerror("Error!","Ha ocurrido un error:"+str(e)) 
            
    def consultadUno(self,ID):                  
        Conexion = self.__conectaBD()
        #Verificamos que el ID no este vacio      
        if(ID == ""):
            messagebox.showwarning("Aviso!","Por favor completa el campo")  
            Conexion.close()
        else: #Procedemos a realizar la consulta
            try:
                Cursor = Conexion.cursor()
                SQL = "SELECT * FROM TBPedimentos WHERE IDExpo="+ID
                Cursor.execute(SQL) #Lanzamos la consulta
                ResultadosCons = Cursor.fetchall() #Guardamos los resultados de la consulta
                Conexion.close()
                return ResultadosCons 
            except sqlite3.OperationalError:
                print("Ha occurido un error en la consulta")  