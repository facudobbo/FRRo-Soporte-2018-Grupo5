import tkinter as tk
from tkinter import *
from tkinter import ttk

def pideCerrar():
    root.destroy()
    root.quit()
def suma():
    nro1=root.nv1.get()
    nro2=root.nv2.get()
    rta=nro1+nro2
    root.nv1.set(rta)
    root.nv2.set(rta)

def resta():
    nro1=root.nv1.get()
    nro2=root.nv2.get()
    rta=nro1-nro2
    root.nv1.set(rta)
    root.nv2.set(rta)

def multip():
    nro1=root.nv1.get()
    nro2=root.nv2.get()
    rta=nro1*nro2
    root.nv1.set(rta)
    root.nv2.set(rta)
def divi():
    nro1=root.nv1.get()
    nro2=root.nv2.get()
    rta=nro1/nro2
    root.nv1.set(rta)
    root.nv2.set(rta)

root=Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.title('Calculadora')

root.marco =ttk.Frame(root, borderwidth=2, relief="raised", padding=(10,10))


root.etiq1= Label(root.marco, text="Primer Operando")
root.nv1=IntVar()
root.nv2=IntVar()

root.nro1= Entry(root.marco, textvariable=root.nv1, width=30)
root.etiq2= Label(root.marco, text="Segundo Operando")
root.nro2= Entry(root.marco, textvariable=root.nv2, width=30)

root.bt1=Button(root.marco,text="+",command=suma)
root.bt2=Button(root.marco,text="-",command=resta)
root.bt3=Button(root.marco,text="*",command=multip)
root.bt4=Button(root.marco,text="/",command=divi)


root.marco.grid(column=0, row=0, padx=5, pady=5, sticky=(N, S, E, W))

root.etiq1.grid(column=0, row=0, sticky=(N, S, E, W), padx=5, pady=5)
root.etiq2.grid(column=1, row=0, sticky=(N, S, E, W), padx=5, pady=5)

root.nro1.grid(column=0, row=1, sticky=(E, W), padx=5, pady=5)
root.nro2.grid(column=1, row=1, sticky=(E, W), padx=5, pady=5)
root.bt1.grid(column=2, row=1, padx=5,sticky=(E,W))
root.bt2.grid(column=3, row=1, padx=5,sticky=(W,E))
root.bt3.grid(column=4, row=1, padx=5,sticky=(E,W))
root.bt4.grid(column=5, row=1, padx=5,sticky=(W,E))


root.protocol("WM_DELETE_WINDOW", pideCerrar)
root.mainloop()
