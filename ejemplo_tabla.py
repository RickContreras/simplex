import tkinter as tk
import pandas as pd

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
    boton_cerrar = tk.Button(ventana_tabla, text="Cerrar", command=ventana_tabla.destroy)
    boton_cerrar.pack()
    
    # Configurar la ventana y otros widgets si es necesario
    ventana_tabla.title("Tabla de Pandas")

    # ...

def crear_primera_ventana():
    ventana_principal = tk.Toplevel()
    
    boton_mostrar_tabla = tk.Button(ventana_principal, text="Mostrar tabla", command=mostrar_tabla)
    boton_mostrar_tabla.pack()
    
    # Configurar la ventana y otros widgets si es necesario
    ventana_principal.title("Ventana principal")
    # ...

# Crear la primera ventana Toplevel
root = tk.Tk()
crear_primera_ventana()
root.mainloop()
