import numpy as np
import matplotlib.pyplot as plt

# Cambia 'ruta_del_archivo.txt' por la ruta real de tu archivo
iter = 3

for i in range(1, iter+1):
    file_path = f'output_{i}.txt'
    print(file_path)


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
