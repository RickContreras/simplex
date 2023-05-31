import customtkinter as ctk
import tkinter as tk

entradas:list=[]

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
            for j in range(num_columnas+3):
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