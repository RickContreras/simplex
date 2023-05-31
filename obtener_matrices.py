import tkinter as tk
import numpy as np

from scipy.optimize import linprog

def obtener_datos(num_columnas, entradas, filas):
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