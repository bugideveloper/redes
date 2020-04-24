from tkinter import filedialog
from tkinter import *
from cliente import *

def browse_button():
    global directorio_path
    nombreDeArchivo = filedialog.askdirectory()
    directorio_path.set(nombreDeArchivo)
    print("La ruta enviada es "+str(nombreDeArchivo))
    print(nombreDeArchivo)
    start_client(nombreDeArchivo)

root = Tk()
directorio_path = StringVar()
lbl1 = Label(master=root,textvariable=directorio_path)
lbl1.grid(row=0, column=1)
button2 = Button(text="Seleccionar", command=browse_button)
button2.grid(row=0, column=3)

mainloop()