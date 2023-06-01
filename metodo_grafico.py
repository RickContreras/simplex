import numpy as np
import customtkinter as ctk
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from obtener_matrices import obtener_datos

def funcion_lineal(x_1, coef_a, coef_b, coef_c):
    y = (coef_c - coef_b*x_1)/coef_a        
    return y

def funcion_constante_y(x, const_a, const_b):
    const = const_b/const_a
    return np.full(x.shape, const)

def constructor_grafico(matrix_A, vect_b):
    coefientes_x_y = []

    x = np.linspace(0, 20, 1000)

    for i in matrix_A:
        for j in i[range(0,2)]:
            coefientes_x_y.append(j)      

    fig = plt.Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 20)
    ax.set_ylim(-1, 20)
    
    for i in range(1,len(coefientes_x_y), 2):
        if coefientes_x_y[i] == 0:
            # caso y = 0
            ax.vlines(x = vect_b[int((i-1)/2)], ymin = 0, ymax = max(x), colors = 'purple')
        elif coefientes_x_y[i-1] == 0:
            # caso x = 0
            y_x0 = funcion_constante_y(x, coefientes_x_y[i], vect_b[int((i-1)/2)])
            ax.plot(x, y_x0)     
        else:
            y = funcion_lineal(x, coefientes_x_y[i], coefientes_x_y[i-1], vect_b[int((i-1)/2)])
            ax.plot(x, y)
    ax.grid(True)
   
    print(coefientes_x_y)
    return fig



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

    fig = constructor_grafico(A, b)

    # Crear un objeto FigureCanvasTkAgg para mostrar la figura en la ventana
    canvas = FigureCanvasTkAgg(fig, master=ventana_grafica)
    canvas.draw()

    # Agregar el widget Canvas a la ventana
    canvas.get_tk_widget().pack()

    # Configurar la ventana y otros widgets si es necesario
    ventana_grafica.title("Gráfica del problema")
