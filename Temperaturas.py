import random


num_ciudades = 3
num_semanas = 4
num_dias = 7


matriz_temperaturas = [[[random.randint(15, 35) for _ in range(num_dias)] for _ in range(num_semanas)] for _ in range(num_ciudades)]


ciudades = ["Ciudad 1", "Ciudad 2", "Ciudad 3"]


for i in range(num_ciudades):
    print(f"Ciudad: {ciudades[i]}")
    for j in range(num_semanas):
        promedio_semana = sum(matriz_temperaturas[i][j]) / num_dias
        print(f"  Semana {j + 1}: Promedio de temperatura = {promedio_semana:.2f}°C")
    print()
