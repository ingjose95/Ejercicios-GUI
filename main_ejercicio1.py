import tkinter as tk

w = tk.Tk()
w.title('Adivina la capital')

miFrame = tk.Frame(w, relief='ridge')
miFrame.config(relief='groove', bd=10)
miFrame.grid()


label = tk.Label(miFrame, text='¿Cuál es la capital de Venezuela?', font=('Comic Sans MS', 12))
label.grid()

varOpcion = tk.IntVar() 


def seleccionar():

    if varOpcion.get()== 1:

        mostrarResultado.config(text='Has seleccionado: Caracas', font=('Comic Sans MS', 12))
    
    elif varOpcion.get() == 2:

        mostrarResultado.config(text='Has seleccionado: Buenos Aires', font=('Comic Sans MS', 12))
    
    elif varOpcion.get() == 3:

        mostrarResultado.config(text='Has seleccionado: Madrid', font=('Comic Sans MS', 12))

    elif varOpcion.get() == 4:

        mostrarResultado.config(text='Has seleccionado: Lima', font=('Comic Sans MS', 12))

    else:

        mostrarResultado.config(text='Has seleccionado: Bogotá', font=('Comic Sans MS', 12))

def borrarOpc():

    varOpcion.set(None)
    mostrarResultado.config(text='')

boton1 = tk.Radiobutton(miFrame, text='Caracas', font=('Comic Sans MS', 10),variable=varOpcion, value=1, command=seleccionar)
boton1.grid(column=0, row=1, sticky='w')

boton2 = tk.Radiobutton(miFrame, text='Buenos Aires', font=('Comic Sans MS', 10), variable=varOpcion, value=2, command=seleccionar)
boton2.grid(column=0, row=2, sticky='w')

boton3 = tk.Radiobutton(miFrame, text='Madrid', font=('Comic Sans MS', 10),  variable=varOpcion, value=3, command=seleccionar)
boton3.grid(column=0, row=3, sticky='w')

boton4 = tk.Radiobutton(miFrame, text='Lima', font=('Comic Sans MS', 10),  variable=varOpcion, value=4, command=seleccionar)
boton4.grid(column=0, row=4, sticky='w')

boton5 = tk.Radiobutton(miFrame, text='Bogotá', font=('Comic Sans MS', 10),  variable=varOpcion, value=5, command=seleccionar)
boton5.grid(column=0, row=5, sticky='w')

reinicio = tk.Button(miFrame, text='Reiniciar', bg='black', fg='white', font=('Comic Sans MS', 10), bd=1, command=borrarOpc)
reinicio.grid(column=0, row=6, sticky='s')

mostrarResultado = tk.Label(miFrame)

mostrarResultado.grid(column=0, row=7, sticky='s')

w.mainloop()