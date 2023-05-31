import tkinter as tk
import customtkinter as ctk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.optimize import linprog

filas:list=[]
entradas:list=[]
num_filas:int=0
num_columnas:int=0
num_variables_involucradas:int=0

def funcion_lineal(x_1, coef_a, coef_b, coef_c):
    z = coef_a*x_1 + coef_b*x_1 - coef_c
    return z

def funcion_constante_y(x, const):
    return np.full(x.shape, const)

# def funcion_constante_x():


def mostrar_grafica():
    c, A, b, tiene_solucion = obtener_datos(num_columnas)
    print("c")
    print(c)
    print("A")
    print(A)
    print("b")
    print(b)
    print("tiene_solución")
    print(tiene_solucion)
    print(A[2, 0], A[2, 1])

    # Crear una nueva ventana Toplevel
    ventana_grafica = ctk.CTkToplevel()

    # Crear datos para la gráfica de ejemplo (puedes reemplazarlo con tus propios datos)
    x = np.linspace(0, b[0], 1000)
    x_1 = np.linspace(0, 10, 1000)
    x_2 = np.linspace(0, 40, 1000)
    y = funcion_lineal(x_1, A[2, 0], A[2, 1], b[2])
    y_1 = funcion_constante_y(x, b[1]) 

    # Crear una figura de matplotlib y agregar una gráfica
    fig = plt.Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.vlines(x = b[0], ymin = 0, ymax = max(x_2), colors = 'purple')
    ax.plot(x, y)
    ax.plot(x, y_1)
    ax.grid(True)

    # Crear un objeto FigureCanvasTkAgg para mostrar la figura en la ventana
    canvas = FigureCanvasTkAgg(fig, master=ventana_grafica)
    canvas.draw()

    # Agregar el widget Canvas a la ventana
    canvas.get_tk_widget().pack()

    # Configurar la ventana y otros widgets si es necesario
    ventana_grafica.title("Gráfica del problema")
    # ...


def generar_filas_columnas(entrada_filas, entrada_columnas, ventana, variables_involucradas):
 
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

        # Generar encabezados         
        label = ctk.CTkLabel(frame_nueva_ventana, text="Ecuaciones\Variables")
        label.grid(row=0, column=0, padx=5, pady=5)

        # Generar X{j}
        for j in range(1,num_columnas + 1):
            label = ctk.CTkLabel(frame_nueva_ventana, text=f"X_{j}")
            label.grid(row=0, column=j, padx=5, pady=5)  
        
        # Generar simbolo, b y lo que va al final
        label = ctk.CTkLabel(frame_nueva_ventana, text="Simbolo")
        label.grid(row=0, column=num_columnas+1, padx=5, pady=5)
        label = ctk.CTkLabel(frame_nueva_ventana, text="b")
        label.grid(row=0, column=num_columnas+2, padx=5, pady=5)

        for i in range(1, num_filas+2):
            # Encabezado de fila
            if(i==1):
                label = ctk.CTkLabel(frame_nueva_ventana, text=f"Función Objetivo:")
            else:
                label = ctk.CTkLabel(frame_nueva_ventana, text=f"Restricción {i-1}:")
            label.grid(row=i, column=0, padx=5, pady=5)

            # Columnas de datos
            for j in range(1, num_columnas+1):
                entry = ctk.CTkEntry(frame_nueva_ventana)
                entry.grid(row=i, column=j, padx=5, pady=5)
                entradas.append(entry)

            # Simbolo igual por cada fila
            label = ctk.CTkLabel(frame_nueva_ventana, text="=")
            label.grid(row=i, column=num_columnas+1, padx=5, pady=5)

            # Resultado por fila
            entry = ctk.CTkEntry(frame_nueva_ventana)
            entry.grid(row=i, column=num_columnas+2, padx=5, pady=5)
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
        valores = [float(entrada.get()) for entrada in entradas]
        iteraciones = len(valores)/(num_columnas+1)
        iteraciones = int(iteraciones)
        for i in range(iteraciones):
        
            filas.append([ x for x in valores[(num_columnas+1)*i:(num_columnas+1)*(i+1)] ])

        matrix=np.array(filas)

        c=matrix[0][:num_columnas]
        A=matrix[1:,:num_columnas]
        b=matrix[1:,num_columnas]

        res=linprog(c,A_eq=A, b_eq=b, method="highs")

        return (c,A,b,res)
    
    except ValueError:
        tk.messagebox.showerror(title="Error", message="Introduzca soló numeros.")

    

def mostrar_tabla():
    # Crear una nueva ventana Toplevel
    
    global num_columnas
    global num_variables_involucradas

    c,A,b,tiene_solucion=obtener_datos(num_columnas)

    columnas =["Z"]
    columnas.extend([f"x{i}" for i in range(1,num_columnas+1)])
    columnas.extend(["Lado derecho"])

    if(tiene_solucion.fun):

        ventana_tabla = ctk.CTkToplevel()

        C=-c[:num_variables_involucradas] 
        Cb=c[num_variables_involucradas:]
        N=A[:,:num_variables_involucradas]
        B=A[:,num_variables_involucradas:]
        inv_B=np.linalg.inv(B)
        tabla=np.zeros((A.shape[0]+1,A.shape[1]+2))
        tabla[0][0]=1
        tabla[0,1:num_variables_involucradas+1]=Cb.dot(inv_B.dot(N))-C
        tabla[0,num_variables_involucradas+1:A.shape[1]+1]=Cb.dot(inv_B)
        tabla[0][A.shape[1]+1]=Cb.dot(inv_B.dot(b.T))
        tabla[1:,1:N.shape[1]+1]=inv_B.dot(N)
        tabla[1:,N.shape[1]+1:A.shape[1]+1]=inv_B
        tabla[1:,A.shape[1]+1]=inv_B.dot(b)
        df=pd.DataFrame(tabla, columns=columnas)
        df=df.where(~((-0.0001<df) & (df<0.0001)), 0)
        # Crear un widget Text donde se mostrará la tabla de Pandas
        text_widget = tk.Text(ventana_tabla, height=5, width=40)
        text_widget.pack()
        
        # Insertar el DataFrame en el widget Text
        text_widget.insert(tk.END, df.to_string(index=False))

        # Agregar un botón debajo del widget Text
        boton_cerrar = ctk.CTkButton(ventana_tabla, text="Continuar", command=ventana_tabla.destroy)
        boton_cerrar.pack()
        
        # Configurar la ventana y otros widgets si es necesario
        ventana_tabla.title("Tabla con Pandas")
    else:
        tk.messagebox.showerror(title="Error", message="Su problema no tiene solución. Replantee los coeficientes.")
    
    
    
    

