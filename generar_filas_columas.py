import tkinter as tk
import customtkinter as ctk
import pandas as pd

entradas:list=[]

def generar_filas_columnas(entrada_filas, entrada_columnas, ventana):
    # print(entrada_filas)
    # print(entrada_columnas)
    try:
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
                        entradas.append(entry)

        boton_generar = tk.Button(frame_nueva_ventana, text="Generar problema", command=obtener_datos)
        boton_generar.grid(row=num_columnas+3, column=((num_columnas+3)//2), padx=5, pady=5)

    except ValueError:
        tk.messagebox.showerror(title="Error", message="Introduzca solo numeros.")

def obtener_datos():
    try:
        valores=[float(entrada.get()) for entrada in entradas]
        print(valores)
    except ValueError:
        tk.messagebox.showerror(title="Error", message="Introduzca solo numeros.")

    

def mostrar_tabla():
    # Crear una nueva ventana Toplevel
    ventana_tabla = tk.Toplevel()
    
    # Crear un DataFrame de ejemplo (puedes reemplazarlo con tus datos)
    datos = {
         'Nombre': ['Juan', 'María', 'Pedro'],
         'Edad': [25, 30, 35],
         'Ciudad': ['Madrid', 'Barcelona', 'Valencia']
     }
    df = pd.DataFrame(datos)
    
    # Crear un widget Text donde se mostrará la tabla de Pandas
    text_widget = tk.Text(ventana_tabla, height=10, width=30)
    text_widget.pack()
    
    # Insertar el DataFrame en el widget Text
    text_widget.insert(tk.END, df.to_string(index=False))

    # Agregar un botón debajo del widget Text
    boton_cerrar = tk.Button(ventana_tabla, text="Continuar", command=ventana_tabla.destroy)
    boton_cerrar.pack()
    
    # Configurar la ventana y otros widgets si es necesario
    ventana_tabla.title("Tabla de Pandas")

    # ...
    
    

