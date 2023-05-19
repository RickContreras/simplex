import tkinter as tk
import customtkinter as ctk

def generar_filas_columnas(entrada_filas, entrada_columnas, ventana):
    # print(entrada_filas)
    # print(entrada_columnas)
    num_filas = int(entrada_filas.get())
    num_columnas = int(entrada_columnas.get())
    
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
                    entry.grid(row=i, column=j, padx=5, pady=5)