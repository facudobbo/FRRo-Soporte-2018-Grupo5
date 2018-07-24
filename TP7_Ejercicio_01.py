from TP5.TP5_Ejercicio_01 import Socio
from TP6.TP6_Ejercicio_01 import NegocioSocio
import tkinter as tk
from tkinter import *
from tkinter import ttk
def alta():
    root=tk.Tk()
    root.title("Nuevo Socio")
    root.marco=ttk.Frame(root, borderwidth=2, relief="raised", padding=(10,10))
    root.marco.grid(column=0, row=0, padx=5, pady=5, sticky=(N, S, E, W))
    root.nom= StringVar()
    root.ape=StringVar()
    root.dni=StringVar()
    root.rotNom=Label(root.marco, text= "Nombre:")
    root.rotAp=Label(root.marco, text= "Apellido:")
    root.rotDni=Label(root.marco, text="DNI:")

    root.EN=ttk.Entry(root.marco, textvariable=root.nom)
    root.EA=ttk.Entry(root.marco, textvariable=root.ape)
    root.ED=ttk.Entry(root.marco, textvariable= root.dni)

    root.bot=ttk.Button(root.marco, text="Aceptar", command=lambda: cargardatos(root))
    root.rotNom.grid(column=0, row=1, sticky=(E, W), padx=5, pady=5)
    root.rotAp.grid(column=0, row=2, sticky=(E, W), padx=5, pady=5)
    root.rotDni.grid(column=0, row=3, sticky=(E, W), padx=5, pady=5)

    root.EN.grid(column=1, row=1, sticky=(E, W), padx=5, pady=5)
    root.EA.grid(column=1, row=2, sticky=(E, W), padx=5, pady=5)
    root.ED.grid(column=1, row=3, sticky=(E, W), padx=5, pady=5)

    root.bot.grid(column=1, row=4, sticky=(E, W), padx=5, pady=5)
    root.mainloop()

def cargardatos(root):
    s= Socio(dni=root.ED.get(), nombre=root.EN.get(), apellido=root.EA.get())

    rta=n.alta(s)
    if rta:
        soc=n.buscar_dni(s.dni)
        c.treeview.insert("", tk.END, text=soc.id, values=(soc.nombre,soc.apellido,soc.dni))
    else:
        print("No funciona")
    root.destroy()
def baja():
    i=c.treeview.focus()
    if i:
        c.treeview.delete(i)
    else:
        a=tk.Tk()
        a.title("Borrar Socio")
        a.marco=ttk.Frame(a, borderwidth=2, relief="raised", padding=(10,10))
        a.marco.grid(column=0, row=0, padx=5, pady=5, sticky=(N, S, E, W))
        a.msj=ttk.Label(a.marco, text="No hay ningun socio seleccionado")
        a.bt=ttk.Button(a.marco, text="Salir", command=lambda: salir(a))
        a.msj.grid(column=0, row=1, sticky=(E, W), padx=5, pady=5)
        a.bt.grid(column=0, row=2, sticky=(E, W), padx=5, pady=5)
        a.mainloop()
def modif():
    i=c.treeview.focus()
    a=tk.Tk()
    a.title("Modificar Socio")
    a.marco=ttk.Frame(a, borderwidth=2, relief="raised", padding=(10,10))
    a.marco.grid(column=0, row=0, padx=5, pady=5, sticky=(N, S, E, W))
    if i:

        datos=c.treeview.item(i,"values")

        a.rotNom=Label(a.marco, text="Nombre:")
        a.rotAp=Label(a.marco, text="Apellido:")
        a.rotDni=Label(a.marco, text="DNI:")

        a.nombre= StringVar()
        a.ape=StringVar()
        a.dni=StringVar()

        a.EN=ttk.Entry(a.marco, textvariable=a.nombre,width=30)
        a.EA=ttk.Entry(a.marco, textvariable=a.ape, width=30)
        a.ED=ttk.Entry(a.marco, textvariable=a.dni, width=30)
        a.EN.insert(0, datos[0])
        a.EA.insert(0,datos[1])
        a.ED.insert(0,datos[2])
        a.bot=ttk.Button(a.marco, text="Aceptar", command=lambda: editar(a,i))
        a.rotNom.grid(column=0, row=1, sticky=(E, W), padx=5, pady=5)
        a.rotAp.grid(column=0, row=2, sticky=(E, W), padx=5, pady=5)
        a.rotDni.grid(column=0, row=3, sticky=(E, W), padx=5, pady=5)

        a.EN.grid(column=1, row=1, sticky=(E, W), padx=5, pady=5)
        a.EA.grid(column=1, row=2, sticky=(E, W), padx=5, pady=5)
        a.ED.grid(column=1, row=3, sticky=(E, W), padx=5, pady=5)

        a.bot.grid(column=1, row=4, sticky=(E, W), padx=5, pady=5)
    else:
        a.msj=ttk.Label(a.marco, text="No hay ningun socio seleccionado")
        a.bt=ttk.Button(a.marco, text="Salir", command=lambda: salir(a))
        a.msj.grid(column=0, row=1, sticky=(E, W), padx=5, pady=5)
        a.bt.grid(column=0, row=2, sticky=(E, W), padx=5, pady=5)
    a.mainloop()

def salir(root):
    root.destroy()
def editar(root,i):
    s= Socio(id=c.treeview.item(i, "text") ,dni=root.ED.get(), nombre=root.EN.get(), apellido=root.EA.get())

    rta=n.modificacion(s)
    if rta:
        c.treeview.item(i, values=(root.EN.get(),root.EA.get(),root.ED.get()))
    else:
        print("No funciona")



    root.destroy()


c=tk.Tk()
c.title("ABM Socios Gestion Socios")
c.marco=ttk.Frame(c, borderwidth=1, relief="raised", padding=(10,10))
c.marco.grid(column=0, row=0, padx=5, pady=5, sticky=(N, S, E, W))
c.treeview = ttk.Treeview(c.marco, selectmode=tk.BROWSE)
c.treeview = ttk.Treeview(c.marco, columns= ("nom", "ape", "dni"))
c.treeview.heading("#0", text="ID")
c.treeview.heading("nom", text="Nombre")
c.treeview.heading("ape", text="Apellido")
c.treeview.heading("dni", text="DNI")
n=NegocioSocio()
for s in n.todos():
    c.treeview.insert("", END, text=s.id, values=(s.nombre,s.apellido, s.dni ))

c.btAlta=Button(c.marco, text="Alta", command=alta)
c.btBaja=Button(c.marco, text="Baja", command=baja)
c.btModif=Button(c.marco, text="Modificar", command=modif)

c.marco.grid(column=0, row=0, padx=5, pady=5, sticky=(N, S, E, W))
c.treeview.grid(column=0, row=0, sticky=(E, W),columnspan=6, padx=5, pady=5)
c.btAlta.grid(column=0, row=1, sticky=(E, W), padx=5, pady=5)
c.btBaja.grid(column=1, row=1, sticky=(E, W), padx=5, pady=5)
c.btModif.grid(column=2, row=1, sticky=(E, W), padx=5, pady=5)

c.mainloop()
