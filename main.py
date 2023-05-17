import tkinter as tk
import customtkinter as ctk
from generar_filas_columas import generar_filas_columnas


# Crear ventana
ventana = tk.Tk()
ventana.title("Metodo Simplex")

# Crear marco
frame = tk.Frame(ventana)
frame.pack(padx=10, pady=10)

# Crear etiquetas y casillas de texto para introducir el número de filas y columnas
label_filas = tk.Label(frame, text="Introduce el número de restricciones:")
label_filas.pack(padx=5, pady=5)

entrada_filas = ctk.CTkEntry(frame)
entrada_filas.pack(padx=5, pady=5)

label_columnas = tk.Label(frame, text="Introduce el número de variables:")
label_columnas.pack(padx=5, pady=5)

entrada_columnas = ctk.CTkEntry(frame)
entrada_columnas.pack(padx=5, pady=5)

# Botón para generar filas y columnas
boton_generar = tk.Button(frame, text="Generar problema", command=generar_filas_columnas(entrada_filas, entrada_columnas, ventana))
boton_generar.pack(padx=5, pady=5)

# Ejecutar ventana
ventana.mainloop()