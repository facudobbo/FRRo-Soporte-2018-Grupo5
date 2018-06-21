import tkinter as tk
from  tkinter import  *
from tkinter import ttk
class Application(ttk.Frame):

    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Codigos Postales")
        self.marco=ttk.Frame(self, borderwidth=2, relief="raised", padding=(10,10))

        self.treeview = ttk.Treeview(self.marco, columns= "cp")
        self.treeview.heading("#0", text="Ciudad")
        self.treeview.heading("cp", text="Codigo Postal")
        self.treeview.insert("", tk.END, text="Rosario", values="2000")
        self.treeview.insert("", tk.END, text="Funes", values="2132")
        self.treeview.insert("", tk.END, text="Roldan", values="2134")
        self.treeview.insert("", tk.END, text="Carcaraña", values="2138")
        self.treeview.insert("", tk.END, text="San Lorenzo", values="2200")

        self.marco.grid(column=0, row=0, padx=5, pady=5, sticky=(N, S, E, W))

        self.treeview.grid(column=0, row=0, sticky=(E, W), padx=5, pady=5)
        self.pack()

main_window = tk.Tk()

app = Application(main_window)
app.mainloop()
