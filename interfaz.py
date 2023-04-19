from tkinter import *
from tkinter import ttk
from miClase import *

#definimos las funciones de la pestania

def guardaPedimento():
    myFunciones = FuncionesBD()
    
    myFunciones.insertaPedimento(txtTransporte.get(),varAduana.get())

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


#pestania 3 Aqui lo relacionado con la consulta
FEntrada = Frame(ConsultaP)
FContenido = Frame(ConsultaP)

LabelTittle3 = Label(ConsultaP,text="Consulta de Pedimentos",font=("Arial", 10, "bold"), fg="#333", bg="#f2f2f2", padx=6, pady=6)
LabelTittle3.pack(pady=padEnY)





#Agregamos las pestanias al notebook
myPanel.add(InsercionP,text="Inserccion de Pedimentos")
myPanel.add(EliminarP,text="Eliminacion de Pedimentos")
myPanel.add(ConsultaP,text="Consulta de Pedimentos")

ventana.mainloop()

