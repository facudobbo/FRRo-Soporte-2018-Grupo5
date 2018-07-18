import tkinter as tk
from tkinter import *
from tkinter import ttk


def alta():
    root=tk.Tk()
    root.title("Nueva Ciudad")
    root.marco=ttk.Frame(root, borderwidth=2, relief="raised", padding=(10,10))
    root.marco.grid(column=0, row=0, padx=5, pady=5, sticky=(N, S, E, W))
    root.ciudad= StringVar()
    root.cod=StringVar()
    root.nciu=Label(root.marco, text= "Ciudad:")
    root.ncp=Label(root.marco, text= "Codigo Postal:")
    root.EC=ttk.Entry(root.marco, textvariable=root.ciudad)
    root.ECod=ttk.Entry(root.marco, textvariable=root.cod)
    root.bot=ttk.Button(root.marco, text="Aceptar", command=lambda: cargardatos(root))
    root.nciu.grid(column=0, row=1, sticky=(E, W), padx=5, pady=5)
    root.ncp.grid(column=0, row=2, sticky=(E, W), padx=5, pady=5)
    root.EC.grid(column=1, row=1, sticky=(E, W), padx=5, pady=5)
    root.ECod.grid(column=1, row=2, sticky=(E, W), padx=5, pady=5)
    root.bot.grid(column=1, row=3, sticky=(E, W), padx=5, pady=5)
    root.mainloop()

def cargardatos(root):
    c.treeview.insert("", tk.END, text=root.EC.get(), values=root.ECod.get())
    root.destroy()


def baja():
    i=c.treeview.focus()
    c.treeview.delete(i)

def modif():
    root=tk.Tk()
    root.title("Modificar Ciudad")
    root.marco=ttk.Frame(root, borderwidth=2, relief="raised", padding=(10,10))
    root.marco.grid(column=0, row=0, padx=5, pady=5, sticky=(N, S, E, W))
    root.cod=StringVar()

    root.ncp=Label(root.marco, text= "Codigo Postal:")
    root.ECod=ttk.Entry(root.marco, textvariable=root.cod)
    root.bot=ttk.Button(root.marco, text="Aceptar", command=lambda: editar(root))

    root.ncp.grid(column=0, row=1, sticky=(E, W), padx=5, pady=5)
    root.ECod.grid(column=1, row=1, sticky=(E, W), padx=5, pady=5)
    root.bot.grid(column=1, row=2, sticky=(E, W), padx=5, pady=5)
    root.mainloop()

def editar(root):
    i=c.treeview.focus()
    c.treeview.item(i, values=root.ECod.get())
    root.destroy()

c=tk.Tk()

c.title("Codigos Postales")
c.marco=ttk.Frame(c, borderwidth=2, relief="raised", padding=(10,10))
c.marco.grid(column=0, row=0, padx=5, pady=5, sticky=(N, S, E, W))
c.treeview = ttk.Treeview(c.marco, selectmode=tk.BROWSE)
c.treeview = ttk.Treeview(c.marco, columns= "cp")
c.treeview.heading("#0", text="Ciudad")
c.treeview.heading("cp", text="Codigo Postal")
c.treeview.insert("", tk.END, text="Rosario", values="2000")
c.treeview.insert("", tk.END, text="Funes", values="2132")
c.treeview.insert("", tk.END, text="Roldan", values="2134")
c.treeview.insert("", tk.END, text="Carcaraña", values="2138")
c.treeview.insert("", tk.END, text="San Lorenzo", values="2200")

c.btAlta=Button(c.marco, text="Alta", command=alta)
c.btBaja=Button(c.marco, text="Baja", command=baja)
c.btModif=Button(c.marco, text="Modificar", command=modif)

c.marco.grid(column=0, row=0, padx=5, pady=5, sticky=(N, S, E, W))
c.treeview.grid(column=0, row=0, sticky=(E, W),columnspan=3, padx=5, pady=5)
c.btAlta.grid(column=0, row=1, sticky=(E, W), padx=5, pady=5)
c.btBaja.grid(column=1, row=1, sticky=(E, W), padx=5, pady=5)
c.btModif.grid(column=2, row=1, sticky=(E, W), padx=5, pady=5)

c.mainloop()


