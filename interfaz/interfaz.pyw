from tkinter import *
#se inicia la instancia de tkinter (interfaz)
raiz = Tk()
#titulo de la ventana
raiz.title("Ventana de pruebas")
#no se puede cambiar tamaño (false, false)
raiz.resizable(True,True)
#tamaño de la ventana
raiz.geometry("1000x250")

miFrame=Frame()
# miFrame.pack(side="left", anchor="n")
miFrame.pack(fill="both", expand="True")
miFrame.config(width=720, height=480, bg="blue")
miFrame.config(relief="sunken")
miFrame.config(bd=35)



#Se establece que escuche al usuario
raiz.mainloop()
