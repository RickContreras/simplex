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




def generar_filas_columnas(entrada_filas, entrada_columnas, ventana, variables_involucradas):
    # print(entrada_filas)
    # print(entrada_columnas)
    try:
        global num_filas
        global num_columnas
        global num_variables_involucradas
        num_filas = int(entrada_filas.get())
        num_columnas = int(entrada_columnas.get())
        num_variables_involucradas= int(variables_involucradas.get())   
        # Crear nueva ventana
        nueva_ventana = ctk.CTkToplevel(ventana)
        nueva_ventana.title("Simplex Aumentado")
        


        # Crear marco en la nueva ventana
        frame_nueva_ventana = ctk.CTkFrame(nueva_ventana)
        frame_nueva_ventana.pack(padx=10, pady=10)
        
        

        for i in range(num_filas+2):
            for j in range(num_columnas+3):
                if (i==0):
                    if(j==0):
                        label = ctk.CTkLabel(frame_nueva_ventana, text="Ecuaciones\Variables")
                        label.grid(row=0, column=0, padx=5, pady=5)
                    elif(j==num_columnas+1):
                        label = ctk.CTkLabel(frame_nueva_ventana, text="Simbolo")
                        label.grid(row=0, column=num_columnas+1, padx=5, pady=5)
                    elif(j==num_columnas+2):
                        label = ctk.CTkLabel(frame_nueva_ventana, text="b")
                        label.grid(row=0, column=num_columnas+2, padx=5, pady=5)
                    else:
                        label = ctk.CTkLabel(frame_nueva_ventana, text=f"X{j}")
                        label.grid(row=0, column=j, padx=5, pady=5)    
                else:
                    if (j==0):

                        if(i==1):
                            label = ctk.CTkLabel(frame_nueva_ventana, text=f"Función Objetivo:")
                            label.grid(row=i, column=j, padx=5, pady=5)
                        else:
                            label = ctk.CTkLabel(frame_nueva_ventana, text=f"Restricción {i-1}:")
                            label.grid(row=i, column=j, padx=5, pady=5)

                    elif(j==num_columnas+1):
                        label = ctk.CTkLabel(frame_nueva_ventana, text="=")
                        label.grid(row=i, column=j, padx=5, pady=5)
                    else:
                        entry = ctk.CTkEntry(frame_nueva_ventana)
                        entry.grid(row=i, column=j, padx=5, pady=5)
                        entradas.append(entry)

        boton_obtener_datos = ctk.CTkButton(frame_nueva_ventana, text="Solucionar", command=mostrar_tabla)
        boton_obtener_datos.grid(row=num_columnas+3, column=((num_columnas+3)//2), padx=5, pady=5)

        if(num_variables_involucradas==2):
            boton_graficar = ctk.CTkButton(frame_nueva_ventana, text="Graficar problema", command=mostrar_grafica)
            boton_graficar.grid(row=num_columnas+3, column=(((num_columnas+3)//2)-1), padx=5, pady=5)


    except ValueError:
        tk.messagebox.showerror(title="Error", message="Introduzca solo numeros enteros.")

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
    
    

