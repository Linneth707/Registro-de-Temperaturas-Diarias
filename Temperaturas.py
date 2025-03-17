import random

# Definir dimensiones de la matriz
num_ciudades = 3  # Número de ciudades
num_semanas = 4    # Número de semanas
num_dias = 7       # Días de la semana

# Crear matriz 3D con temperaturas aleatorias entre 15 y 35 grados
matriz_temperaturas = [[[random.randint(15, 35) for _ in range(num_dias)] for _ in range(num_semanas)] for _ in range(num_ciudades)]

# Lista de nombres de ciudades
ciudades = ["Ciudad 1", "Ciudad 2", "Ciudad 3"]

# Abrir un archivo para guardar los resultados
with open("resultado.txt", "w") as archivo:
    for i in range(num_ciudades):
        archivo.write(f"Ciudad: {ciudades[i]}\n")
        for j in range(num_semanas):
            promedio_semana = sum(matriz_temperaturas[i][j]) / num_dias
            archivo.write(f"  Semana {j + 1}: Promedio de temperatura = {promedio_semana:.2f}°C\n")
        archivo.write("\n")

print("El resultado ha sido guardado en 'resultado.txt'.")



