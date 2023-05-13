#Importaciones
import tkinter as tk

#Creación de la ventana principal
root = tk.Tk()

#Creación de la etiqueta
mensaje = tk.Label(root, text="Mi primer programa con Tkinter.")
#Muestra la etiqueta
mensaje.pack()

#Bucle de ejecución
root.mainloop()