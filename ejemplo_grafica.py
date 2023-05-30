import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
def mostrar_grafica():
    # Crear una nueva ventana Toplevel
    ventana_grafica = tk.Toplevel()

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
    ventana_grafica.title("Gráfica de ejemplo")
    # ...

def crear_primera_ventana():
    ventana_principal = tk.Toplevel()

    boton_mostrar_grafica = tk.Button(ventana_principal, text="Mostrar gráfica", command=mostrar_grafica)
    boton_mostrar_grafica.pack()

    # Configurar la ventana y otros widgets si es necesario
    ventana_principal.title("Ventana principal")
    # ...

# Crear la primera ventana Toplevel
root = tk.Tk()
crear_primera_ventana()
root.mainloop()
