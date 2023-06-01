import tkinter as tk
import customtkinter as ctk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from obtener_matrices import obtener_datos
from metodo_grafico import mostrar_grafica

filas:list=[]
entradas:list=[]
num_filas:int=0
num_columnas:int=0
num_variables_involucradas:int=0

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

            def funcion_mostrar_graf():
                return mostrar_grafica(num_columnas, entradas, filas)

            boton_graficar = ctk.CTkButton(frame_nueva_ventana, text="Graficar problema", command=funcion_mostrar_graf)
            boton_graficar.grid(row=num_columnas+3, column=(((num_columnas+3)//2)-1), padx=5, pady=5)


    except ValueError:
        tk.messagebox.showerror(title="Error", message="Introduzca solo numeros enteros.")
        
    

def mostrar_tabla():
    # Crear una nueva ventana Toplevel
    
    global num_columnas
    global num_variables_involucradas
    global entradas
    
    c,A,b,tiene_solucion=obtener_datos(num_columnas, entradas, filas)
    tablas=[]
    columnas =["Z"]
    columnas.extend([f"x{i}" for i in range(1,num_columnas+1)])
    columnas.extend(["Lado derecho"])

    if(tiene_solucion.fun):
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
        tablas.append(df)
        for i in range(2): #Esto se debe cambiar es solo particular para este problema.
            Cb[i] =C[i].copy()
            B[:,i]=N[:,i].copy()
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
            df=df.where(~((-0.0001<df) & (df<0.0001)), 0).round(2)
            tablas.append(df)
        # Crear un widget Text donde se mostrará la tabla de Pandas
        
        for i in range(len(tablas)):

            df=tablas[i]
            ventana_tabla = ctk.CTkToplevel()
            text_widget = tk.Text(ventana_tabla, height=8, width=45)
            text_widget.pack()
            
            # Insertar el DataFrame en el widget Text
            text_widget.insert(tk.END, df.to_string(index=False))
            
            # Configurar la ventana y otros widgets si es necesario
            ventana_tabla.title(f"Tabla {i+1}")

        
    else:
        tk.messagebox.showerror(title="Error", message="Su problema no tiene solución. Replantee los coeficientes.")
    
    
    
    

