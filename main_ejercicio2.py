import tkinter as tk

w = tk.Tk()


azucar = tk.IntVar()
leche = tk.IntVar()
harina = tk.IntVar()
huevos = tk.IntVar()
cafe = tk.IntVar()

lista= tk.Label(w, text='Lista de compras')
lista.grid()

def mostrar():

    mostrarOpciones = ''

    if azucar.get()==1:

        mostrarOpciones += ' Azucar'

    if leche.get() == 1:

        mostrarOpciones += ' Leche'

    if harina.get() == 1:

        mostrarOpciones += ' Harina'

    if huevos.get() == 1:

        mostrarOpciones += ' Huevos'

    if cafe.get() == 1:

        mostrarOpciones += ' Cafe'

    caja.config(text=mostrarOpciones)


opcion = tk.Checkbutton(w, text='Azucar',variable=azucar, offvalue=0, onvalue=1, command=mostrar).grid(sticky='w')
opcion = tk.Checkbutton(w, text='Leche', variable=leche, offvalue=0, onvalue=1, command=mostrar).grid(sticky='w')
opcion = tk.Checkbutton(w, text='Harina', variable=harina, offvalue=0, onvalue=1, command=mostrar).grid(sticky='w')
opcion = tk.Checkbutton(w, text='Huevos', variable=huevos, offvalue=0, onvalue=1, command=mostrar).grid(sticky='w')
opcion = tk.Checkbutton(w, text='Café', variable=cafe, offvalue=0,onvalue=1, command=mostrar).grid(sticky='w')

caja = tk.Label(w)
caja.grid()



w.mainloop()