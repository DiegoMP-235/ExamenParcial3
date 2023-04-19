from tkinter import *
from tkinter import ttk
import tkinter as tk
from miClase import *

#definimos las funciones de la pestania

def guardaPedimento():
    myFunciones = FuncionesBD()
    
    myFunciones.insertaPedimento(txtTransporte.get(),varAduana.get())

def limpiaArbol():
    #limpiamos el arbol
    for i in tree.get_children():
        tree.delete(i) 
        
def consultaPedimento():
    myFunciones = FuncionesBD()
    Aduana = varAduanaC.get()
    print(Aduana)
    rows = myFunciones.consultaPedimento(Aduana)
    
    if(len(rows) < 1):
        messagebox.showinfo("No se encontraron resultados","No se encontraron resultados\nPuedes agregar en la pestania de insercion")
        return
    #limpiamos el arbol 
    limpiaArbol()
    #insertamos los resultados en el arbol    
    for Usuario in rows:
        tree.insert("",END,values=(Usuario[0],Usuario[1],Usuario[2]))        

def eliminaPedimento():
    myFunciones = FuncionesBD()
    ID = txtIDDel.get()
    Resultados = myFunciones.consultadUno(ID)
    if(len(Resultados) < 1):
        messagebox.showinfo("No se encontraron resultados","Este id no se encontro en la base de datos")
        return
    
    myFunciones.eliminaPedimento(ID)
    #limpiamos el arbol
    limpiaArbol()
    

ventana = Tk()
ventana.title("Sistema de Aduanas")
ventana.geometry('480x320')
padEnY = 8

#instanciamos un notebook
myPanel = ttk.Notebook(ventana)
myPanel.pack(fill="both",expand=True)
InsercionP = ttk.Frame(myPanel)
EliminarP = ttk.Frame(myPanel)
ConsultaP = ttk.Frame(myPanel)

#Agregaos los widgets a las pestanias
LabelTittle = Label(InsercionP,text="Registro de Pedimentos",font=("Arial", 10, "bold"), fg="#333", bg="#f2f2f2", padx=6, pady=6)
LabelTittle.pack(pady=padEnY)

LblTrans = Label(InsercionP,text="Trasnporte:")
LblTrans.pack(pady=padEnY)

txtTransporte = Entry(InsercionP)
txtTransporte.pack(pady=padEnY)

LblAduana = Label(InsercionP,text="Aduana:")
LblAduana.pack(pady=padEnY)

varAduana = StringVar()
Aduanas = ["Terrestre","Maritima","Area"]
varAduana.set(Aduanas[0])
selAduana = ttk.Combobox(InsercionP,textvariable=varAduana,values=Aduanas)
selAduana.pack(pady=padEnY)

#txtAduana = Entry(InsercionP)
#txtAduana.pack()

BtnGuardar = Button(InsercionP,text="Guardar",command=guardaPedimento)
BtnGuardar.pack(pady=padEnY)

#aqui lo relacionado con la pestania de eliminacion
LabelTittle2 = Label(EliminarP,text="Eliminacion de Pedimentos",font=("Arial", 10, "bold"), fg="#333", bg="#f2f2f2", padx=6, pady=6)
LabelTittle2.pack(pady=padEnY)

LblIDDel = Label(EliminarP,text="ID a eliminar:")
LblIDDel.pack(pady=padEnY)

txtIDDel = Entry(EliminarP)
txtIDDel.pack(pady=padEnY)
"""
LblTransporte = Label(EliminarP,text="Trasnporte:")
LblTransporte.pack(pady=padEnY)

LblAduanaDel =Label(EliminarP,text="Aduana:")
LblAduanaDel.pack(pady=padEnY)
"""


BtnDel = Button(EliminarP,text="Eliminar",command=eliminaPedimento)
BtnDel.pack(pady=padEnY)

#pestania 3 Aqui lo relacionado con la consulta
#FEntrada = Frame(ConsultaP)
#FContenido = Frame(ConsultaP)

LabelTittle3 = Label(ConsultaP,text="Consulta de Pedimentos",font=("Arial", 10, "bold"), fg="#333", bg="#f2f2f2", padx=6, pady=6)
LabelTittle3.pack(pady=padEnY)

varAduanaC = StringVar()
varAduanaC.set(Aduanas[0])
consAduana = ttk.Combobox(ConsultaP,textvariable=varAduanaC,values=Aduanas)
consAduana.pack(pady=padEnY)

BtnConsAdu = Button(ConsultaP,text="Consultar",command=consultaPedimento)
BtnConsAdu.pack(pady=padEnY)

#Aqui se mostraran los resultados
#Scrollbar vertical
scrollbar = tk.Scrollbar(ConsultaP,orient="vertical")
scrollbar.pack(side=RIGHT,fill=Y)

#scrollbar horizontal
scrollbar2 = tk.Scrollbar(ConsultaP,orient="horizontal")
scrollbar2.pack(side="bottom",fill=X)

#Ponemos encabezados de los campos de la bd
Columnas = ('ID','Transporte','Aduana')
tree = ttk.Treeview(ConsultaP,columns=Columnas,show='headings',yscrollcommand=scrollbar.set,xscrollcommand=scrollbar2.set)
tree.heading('ID', text='ID')
tree.heading('Transporte', text='Transporte')
tree.heading('Aduana', text='Aduana')
tree.pack(fill='both', expand=True)

#Configuramos el scroll
scrollbar.config(command=tree.yview)
scrollbar2.config(command=tree.xview)



#Agregamos las pestanias al notebook
myPanel.add(InsercionP,text="Inserccion de Pedimentos")
myPanel.add(EliminarP,text="Eliminacion de Pedimentos")
myPanel.add(ConsultaP,text="Consulta de Pedimentos")

ventana.mainloop()

