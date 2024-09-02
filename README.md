# 📊 Aplicación de Programación Lineal con Método Simplex

Esta aplicación con interfaz gráfica permite resolver problemas de programación lineal utilizando el método Simplex. La interfaz facilita la entrada de datos, la visualización de resultados y la generación de gráficos.


## 🚀 Características

- Implementación del método Simplex en Python.
- Interfaz gráfica de usuario (GUI) con Tkinter y CustomTkinter.
- Visualización de datos con Matplotlib.
- Soporte para múltiples tipos de problemas de programación lineal.

## 📋 Requisitos

- Python 3.x
- Tkinter
- CustomTkinter
- Matplotlib
- Pandas
- Numpy

## 📥 Instalación

Sigue estos pasos para instalar y configurar el entorno del proyecto:

1. **Clona el repositorio:**
    ```bash
    git clone https://github.com/RickContreras/simplex.git
    ```
    Esto descargará una copia del repositorio en tu máquina local.

2. **Navega al directorio del proyecto:**
    ```bash
    cd simplex
    ```
    Cambia al directorio del proyecto recién clonado.

3. **Crea un entorno virtual:**
    ```bash
    python3 -m venv venv
    ```
    Esto creará un entorno virtual aislado llamado `venv`.

4. **Activa el entorno virtual:**
    - **En Windows:**
      ```bash
      .\venv\Scripts\activate
      ```
    - **En macOS/Linux:**
      ```bash
      source venv/bin/activate
      ```

5. **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
    Esto instalará todas las dependencias necesarias listadas en el archivo `requirements.txt`.

6. **Verifica la instalación:**
    ```bash
    python --version
    pip list
    ```
    Asegúrate de que Python y las bibliotecas necesarias estén correctamente instaladas.

7. **Ejecuta la aplicación:**
    ```bash
    python main.py
    ```
    Esto iniciará la aplicación y abrirá la interfaz gráfica de usuario.

## 🖥️ Uso

1. **Activa el entorno virtual**  
   Asegúrate de que el entorno virtual esté activado utilizando el comando correspondiente a tu sistema operativo.
    - **En Windows:** .\venv\Scripts\activate
    - **En macOS/Linux:** source venv/bin/activate

2. **Inicia la aplicación**  
   Ejecuta el script principal:
    ```bash
    python main.py
    ```

3. **Interacción con la GUI**  
   Utiliza la interfaz gráfica para ingresar los datos del problema de programación lineal. La aplicación te permitirá definir restricciones, objetivos y variables.

4. **Visualiza los resultados**  
   La aplicación mostrará los resultados y las gráficas generadas para el problema resuelto.

## 📁 Estructura del Proyecto

- **`main.py`**: Archivo principal que inicia la aplicación y contiene la configuración de la interfaz gráfica.

- **`funciones_simplex.py`**: Contiene las funciones necesarias para la implementación del método Simplex.

- **`requirements.txt`**: Lista de dependencias necesarias para ejecutar el proyecto.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue estos pasos para contribuir:

1. Haz un fork del repositorio.

2. Crea una nueva rama:
   ```bash
    git checkout -b feature/nueva-caracteristica
   ```

3. Realiza los cambios necesarios y haz commit:
  ```bash
  git commit -m 'Agrega nueva característica'
  ```

4. Sube los cambios a tu repositorio:
  ```bash
    git push origin feature/nueva-caracteristica
  ```

5. Abre un Pull Request en el repositorio original.

## 👤 Autores

- [@Sara Galvan](https://github.com/galvanic90)
- [@Ricardo Contreras](https://github.com/Ricardoy568)