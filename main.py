import tkinter as tk
import customtkinter as ctk
from funciones_simplex import generar_filas_columnas

ctk.set_appearance_mode("system")
# Crear ventana
ventana = ctk.CTk()
ventana.title("Metodo Simplex")

# Crear marco
frame = ctk.CTkFrame(ventana)
frame.pack(padx=10, pady=10)

# Crear etiquetas y casillas de texto para introducir el número de filas y columnas
label_filas = ctk.CTkLabel(frame, text="Introduce el número de restricciones:")
label_filas.pack(padx=5, pady=5)

entrada_filas = ctk.CTkEntry(frame)
entrada_filas.pack(padx=5, pady=5)

label_columnas = ctk.CTkLabel(frame, text="Introduce el número de variables:")
label_columnas.pack(padx=5, pady=5)

entrada_columnas = ctk.CTkEntry(frame)
entrada_columnas.pack(padx=5, pady=5)


label_variables_involucradas = ctk.CTkLabel(frame, text="Introduce el número de variables interpretables:")
label_variables_involucradas.pack(padx=5, pady=5)
variables_involucradas= ctk.CTkEntry(frame)
variables_involucradas.pack(padx=5, pady=5)

def generadora_funcion():
    return generar_filas_columnas(entrada_filas, entrada_columnas, ventana, variables_involucradas)


# Botón para generar filas y columnas
boton_generar = ctk.CTkButton(frame, text="Generar problema", command=generadora_funcion)
boton_generar.pack(padx=5, pady=5)

# Ejecutar ventana
ventana.mainloop()