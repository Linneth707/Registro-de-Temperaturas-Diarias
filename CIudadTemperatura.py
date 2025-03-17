from typing import Any


def calcular_promedio_temperaturas(min_temp, max_temp, dias):
    """
    Calcula el promedio de temperaturas para un período dado.

    :param min_temp: Temperatura mínima diaria (en °C).
    :param max_temp: Temperatura máxima diaria (en °C).
    :param dias: Número de días para calcular el promedio (en este caso, 13 días).
    :return: El promedio de las temperaturas durante el período.
    """
    promedio_diario: float | Any = (min_temp + max_temp) / 2  # Promedio diario de las temperaturas
    promedio_total = promedio_diario * dias  # Promedio total durante todos los días
    return promedio_total / dias  # El promedio final


# Datos proporcionados para Quito
minima = 8.9  # Temperatura mínima (°C)
maxima = 17.2  # Temperatura máxima (°C)
dias = 13  # Días desde el 1 de marzo hasta el 13 de marzo de 2025

# Calcular el promedio de las temperaturas
promedio_quito = calcular_promedio_temperaturas(minima, maxima, dias)

# Mostrar el resultado
print(f'La temperatura promedio en Quito del 1 de marzo al 13 de marzo de 2025 es: {promedio_quito:.2f} °C')