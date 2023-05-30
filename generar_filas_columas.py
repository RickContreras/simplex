import tkinter as tk
import pandas as pd
import numpy as np
import customtkinter as ctk

def generar_filas_columnas(entrada_filas, entrada_columnas, ventana):
   
    num_filas = int(entrada_filas.get())
    num_columnas = int(entrada_columnas.get())
    casillas = []

    # Crear nueva ventana
    nueva_ventana = tk.Toplevel(ventana)
    nueva_ventana.title("Simplex Aumentado")
    
    # Crear marco en la nueva ventana
    frame_nueva_ventana = tk.Frame(nueva_ventana)
    frame_nueva_ventana.pack(padx=10, pady=10)
    
    for i in range(num_filas+2):
        for j in range(num_columnas+3):
            if (i==0):
                if(j==0):
                    label = tk.Label(frame_nueva_ventana, text="Restricciones\\Variables")
                    label.grid(row=0, column=0, padx=5, pady=5)
                elif(j==num_columnas+1):
                    label = tk.Label(frame_nueva_ventana, text="Simbolo")
                    label.grid(row=0, column=num_columnas+1, padx=5, pady=5)
                elif(j==num_columnas+2):
                    label = tk.Label(frame_nueva_ventana, text="b")
                    label.grid(row=0, column=num_columnas+2, padx=5, pady=5)
                else:
                    label = tk.Label(frame_nueva_ventana, text=f"X{j}")
                    label.grid(row=0, column=j, padx=5, pady=5)    
            else:
                if (j==0):
                    label = tk.Label(frame_nueva_ventana, text=f"Ecuación {i-1}:")
                    label.grid(row=i, column=j, padx=5, pady=5)
                elif(j==num_columnas+1):
                    label = tk.Label(frame_nueva_ventana, text="=")
                    label.grid(row=i, column=j, padx=5, pady=5)
                else:
                    entry = ctk.CTkEntry(frame_nueva_ventana)
                    
                    casillas.append(entry)
                    entry.grid(row=i, column=j, padx=5, pady=5)
    
    print(casillas)
    return casillas, num_filas, num_columnas

def obtener_coeficientes(casillas, num_filas, num_columnas):
    filas = []
    # for i in range():

    # array_casillas = np.array(casillas)

    for i in range(0, num_filas):

        fila = casillas[i*num_columnas:(i+1)*num_columnas]
        filas.append(filas)



