# 🔹 Objetivo
# Desarrollar un programa en Python que permita ingresar una matriz cuadrada de orden n y determine si es un cuadrado mágico.
# 🔹 Requisitos del Programa
# ✔️ Ingreso de datos:
# Permitir que el usuario ingrese la matriz manualmente o, de manera opcional, generar una aleatoria.
# Validar que los valores ingresados sean números enteros en el rango de 1 a n² y que no se repitan.
# Asegurar que la matriz ingresada tenga un tamaño válido (n × n).


# ✔️ Verificación del cuadrado mágico:
# Calcular la constante mágica según la fórmula.
# Comparar la suma de:
# Cada fila
# Cada columna
# Las dos diagonales principales
# Determinar si todas las sumas son iguales a la constante mágica.
# ✔️ Salida de resultados:
# Mostrar la matriz ingresada de forma clara y organizada.
# Indicar si la matriz es un cuadrado mágico o no.




# 📌 Extras opcionales:
#  ✅ Permitir que el usuario ingrese matrices de distintos tamaños (por ejemplo, 3×3, 4×4, etc.).
#  ✅ Mostrar mensajes de error en caso de ingreso inválido.
#  ✅ Implementar una opción para generar un cuadrado mágico válido automáticamente.

import random

def es_cuadrado_magico(matriz):
    n = len(matriz)
    suma_magica = n * (n**2 + 1) // 2

    for fila in matriz:
        if sum(fila) != suma_magica:
            return False

    for col in range(n):
        if sum(matriz[fila][col] for fila in range(n)) != suma_magica:
            return False

    if sum(matriz[i][i] for i in range(n)) != suma_magica:
        return False

    if sum(matriz[i][n - 1 - i] for i in range(n)) != suma_magica:
        return False

    return True

def validar_matriz(matriz):
    n = len(matriz)
    elementos = set()

    for fila in matriz:
        for elemento in fila:
            if not isinstance(elemento, int):
                print(f"ERROR: El elemento '{elemento}' no es un número entero válido.")
                exit()
            if elemento < 1 or elemento > n**2:
                print(f"ERROR: El número {elemento} no corresponde a ningún producto.")
                exit()
            if elemento in elementos:
                print(f"ERROR: El número {elemento} se repite en la matriz.")
                exit()
            elementos.add(elemento)
            return True
        

def mostrar_matriz(matriz):
    for fila in matriz:
        print(" | ".join(str(elemento) for elemento in fila))
        print("-" * (len(fila) * 4 - 3))


def generar_matriz_aleatoria(n):
    elementos = list(range(1, n**2 + 1))
    random.shuffle(elementos)
    matriz = [elementos[i:i + n] for i in range(0, n**2, n)]
    return matriz


matriz_ingresada = input("¿Desea ingresar la Matriz manualmente o generarla aleatoriamente? (1 = manual, 2 = aleatoria): ")
if matriz_ingresada == "1":
    filas = int(input("Ingrese la cantidad de filas y columnas: "))
    columnas = filas
    if filas != columnas:
        print("ERROR: La matriz no es cuadrada.")
        exit()

elif matriz_ingresada == "2": 
    filas = [random.randint(1, 10) for _ in range(2)]
    columnas = filas
    print("La matriz será generada aleatoriamente.")


matriz = []
for i in range(filas):
    fila = input(f"Ingrese la fila {i + 1} (separados por comas): ").split(",")
    fila = [int(num.strip()) for num in fila]
    matriz.append(fila)
    if len(fila) != columnas:
        print("ERROR: La matriz no es cuadrada.")
        exit()

if not validar_matriz(matriz):
    print("ERROR: La matriz no es válida.")
    exit()
    
mostrar_matriz(matriz)
if es_cuadrado_magico(matriz):
    print("La matriz es un cuadrado mágico.")
else:
    print("La matriz no es un cuadrado mágico.")

