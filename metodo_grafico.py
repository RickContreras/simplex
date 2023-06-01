import numpy as np
import customtkinter as ctk
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from obtener_matrices import obtener_datos

def funcion_lineal(x_1, coef_a, coef_b, coef_c):
    y = (coef_c - coef_b*x_1)/coef_a        
    return y

def funcion_constante_y(x, const_a, const_b):
    const = const_a/const_b
    return np.full(x.shape, const)

def constructor_grafico(matrix_A, vect_b):
    
    x = np.linspace(0, vect_b, 1000)
    x_1 = np.linspace(0, 10, 1000)
    x_2 = np.linspace(0, 40, 1000)
    
    fig = plt.Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.vlines(x = vect_b, ymin = 0, ymax = max(x_2), colors = 'purple')
    ax.plot(x, y)   
    ax.grid(True)



def mostrar_grafica(num_columnas, entradas, filas):

    c, A, b, tiene_solucion = obtener_datos(num_columnas, entradas, filas)
    print("c")
    print(c)
    print("A")
    print(A)
    print("b")
    print(b)
    print("tiene_solución")
    print(tiene_solucion)

    # Crear una nueva ventana Toplevel
    ventana_grafica = ctk.CTkToplevel()
    
    # x_equal_to_zero = params_1[0] == 0
    # y_equal_to_zero = params_1[1] == 0

    # if x_equal_to_zero:
    #     # wait think better about this!
    #     # y_1 = funcion_constante_y(x, b[1], params[1]) 
    #     # ax.plot(x, y_1)
    # y = funcion_lineal(x_1, A[2, 0], A[2, 1], b[2])
    

    # Crear una figura de matplotlib y agregar una gráfica

    # Change this part!!!
    # fig = plt.Figure(figsize=(6, 4), dpi=100)
    # ax = fig.add_subplot(111)
    # ax.vlines(x = b[0], ymin = 0, ymax = max(x_2), colors = 'purple')
    # ax.plot(x, y)   
    # ax.grid(True)

    # Crear un objeto FigureCanvasTkAgg para mostrar la figura en la ventana
    canvas = FigureCanvasTkAgg(fig, master=ventana_grafica)
    canvas.draw()

    # Agregar el widget Canvas a la ventana
    canvas.get_tk_widget().pack()

    # Configurar la ventana y otros widgets si es necesario
    ventana_grafica.title("Gráfica del problema")
    # ...
