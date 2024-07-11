import numpy as np
import matplotlib.pyplot as plt
import os

# Ruta del directorio que quieres verificar
directorio = './output/'
# Obtener la lista de archivos en el directorio
archivos = os.listdir(directorio)
# Contar la cantidad de archivos
cantidadArchivos = len(archivos)


time = np.zeros(cantidadArchivos)
size = np.zeros(cantidadArchivos)


for archivo in archivos:

    timeArray, sizeArray = np.genfromtxt(f'./output/{archivo}',delimiter=' ', usecols=(0,1),unpack=True)
    print(timeArray)
    print(sizeArray)


# # Leer las columnas del archivo .txt
# data = np.loadtxt(file_path, skiprows=1)

# # Separar las columnas en variables individuales
# orden = data[:, 0]
# error = data[:, 1]

# # Verificar si las columnas se han leído correctamente
# print(f"Orden: {orden[:5]}")
# print(f"Error: {error[:5]}")

# plt.figure(figsize=(10, 6))
# plt.plot(orden, error, marker='o', linestyle='-', color='b')

# # Agregar títulos y etiquetas
# plt.title('Gráfica de Orden vs Error')
# plt.xlabel('Orden')
# plt.ylabel('Error')

# # Mostrar la gráfica
# plt.grid(True)
# plt.show()
