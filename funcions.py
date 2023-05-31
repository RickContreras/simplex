import tkinter as tk
import customtkinter as ctk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

filas:list=[]
entradas:list=[]
num_filas:int=0
num_columnas:int=0
num_variables_involucradas:int=0


def mostrar_grafica():
    # Crear una nueva ventana Toplevel
    ventana_grafica = ctk.CTkToplevel()

    # Crear datos para la gráfica de ejemplo (puedes reemplazarlo con tus propios datos)
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    # Crear una figura de matplotlib y agregar una gráfica
    fig = plt.Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(x, y)

    # Crear un objeto FigureCanvasTkAgg para mostrar la figura en la ventana
    canvas = FigureCanvasTkAgg(fig, master=ventana_grafica)
    canvas.draw()

    # Agregar el widget Canvas a la ventana
    canvas.get_tk_widget().pack()

    # Configurar la ventana y otros widgets si es necesario
    ventana_grafica.title("Gráfica del problema")
    # ...



def obtener_datos(num_columnas):
    try:
        valores=[float(entrada.get()) for entrada in entradas]
        iteraciones=len(valores)/(num_columnas+1)
        iteraciones=int(iteraciones)
        for i in range(iteraciones):
        
            filas.append([ x for x in valores[(num_columnas+1)*i:(num_columnas+1)*(i+1)] ])

        print(filas)
    except ValueError:
        tk.messagebox.showerror(title="Error", message="Introduzca soló numeros.")

    

def mostrar_tabla():
    # Crear una nueva ventana Toplevel
    
    global num_columnas

    ventana_tabla = ctk.CTkToplevel()
    

    obtener_datos(num_columnas)

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
    boton_cerrar = ctk.CTkButton(ventana_tabla, text="Continuar", command=ventana_tabla.destroy)
    boton_cerrar.pack()
    
    # Configurar la ventana y otros widgets si es necesario
    ventana_tabla.title("Tabla con Pandas")

    # ...
    
    

