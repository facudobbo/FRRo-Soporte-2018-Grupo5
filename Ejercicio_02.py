from tkinter import *
from tkinter import ttk

def cero():
    root.txt.set('0')
def uno():
    tx=root.txt.get()
    root.txt.set(tx+'1')
def dos():
    tx=root.txt.get()
    root.txt.set(tx+'2')
def tres():
    tx=root.txt.get()
    root.txt.set(tx+'3')
def cuatro():
    tx=root.txt.get()
    root.txt.set(tx+'4')
def cinco():
    tx=root.txt.get()
    root.txt.set(tx+'5')
def seis():
    tx=root.txt.get()
    root.txt.set(tx+'6')
def siete():
    tx=root.txt.get()
    root.txt.set(tx+'7')
def ocho():
    tx=root.txt.get()
    root.txt.set(tx+'8')
def nueve():
    tx=root.txt.get()
    root.txt.set(tx+'9')
def suma():
    tx=root.txt.get()
    root.txt.set(tx+'+')
def resta():
    tx=root.txt.get()
    root.txt.set(tx+'-')
def div():
    tx=root.txt.get()
    root.txt.set(tx+'/')
def mult():
    tx=root.txt.get()
    root.txt.set(tx+'x')
def igu():
    tx=root.txt.get()
    root.txt.set(eval(tx))

def de():
    root.txt.set(str())


root=Tk()

root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)
root.marco =ttk.Frame(root, borderwidth=2, relief="raised", padding=(10,10))

root.title('Calculadora')
root.txt=StringVar()
nro= Entry(root.marco, textvariable=root.txt)
bt0=Button(root.marco,text="0",command=cero)
bt1=Button(root.marco,text="1",command=uno)
bt2=Button(root.marco,text="2",command=dos)
bt3=Button(root.marco,text="3",command=tres)
bt4=Button(root.marco,text="4",command=cuatro)
bt5=Button(root.marco,text="5",command=cinco)
bt6=Button(root.marco,text="6",command=seis)
bt7=Button(root.marco,text="7",command=siete)
bt8=Button(root.marco,text="8",command= ocho)
bt9=Button(root.marco,text="9",command= nueve)
mas=Button(root.marco, text="+", command=suma)
menos=Button(root.marco, text="-",command=resta)
divi=Button(root.marco,text="/", command=div)
multi=Button(root.marco, text="x", command=mult)
igual=Button(root.marco,text="=", command=igu)
c=Button(root.marco,text="AC", command=de)

root.marco.grid(column=0, row=0, padx=5, pady=5, sticky=(N, S, E, W))
nro.grid(column=0, row=0, sticky=(E, W),columnspan=4, padx=5, pady=5)
bt7.grid(column=0,row=1, sticky=(E, W), padx=5, pady=5)
bt8.grid(column=1,row=1, sticky=(E, W), padx=5, pady=5)
bt9.grid(column=2,row=1, sticky=(E, W), padx=5, pady=5)
bt4.grid(column=0,row=2, sticky=(E, W), padx=5, pady=5)
bt5.grid(column=1,row=2, sticky=(E, W), padx=5, pady=5)
bt6.grid(column=2,row=2, sticky=(E, W), padx=5, pady=5)
bt1.grid(column=0, row=3, sticky=(E, W), padx=5, pady=5)
bt2.grid(column=1, row=3, sticky=(E, W), padx=5, pady=5)
bt3.grid(column=2, row=3, sticky=(E, W), padx=5, pady=5)
bt0.grid(column=0, row=4, sticky=(E, W), padx=5, pady=5)
igual.grid(column=1, row=4, sticky=(E, W),columnspan=2, padx=5, pady=5)
mas.grid(column=3, row=1, sticky=(E,W), padx= 5, pady=5)
menos.grid(column=3, row=2, sticky=(E,W), padx= 5, pady=5)
divi.grid(column=3, row=3, sticky=(E,W), padx= 5, pady=5)
multi.grid(column=3, row=4, sticky=(E,W), padx= 5, pady=5)
c.grid(column=4, row=1, sticky=(E,W), rowspan=4, padx=5, pady=5)

root.mainloop()
