def validar_lista(lista):
    for elemento in lista:
        if not elemento.strip().isdigit():
            print(f"ERROR: El elemento '{elemento}' no es un número entero válido.")
            exit()
        if not 1 <= int(elemento.strip()) <= 10:
            print(f"ERROR: El número {elemento.strip()} no corresponde a ningún producto.")
            exit()

def obtener_nombre_producto(numero):
    productos = {
        '1': 'Remera',
        '2': 'Pantalon',
        '3': 'Zapatillas',
        '4': 'Buzo',
        '5': 'Campera',
        '6': 'Gorra',
        '7': 'Guantes',
        '8': 'Medias',
        '9': 'Cinto',
        '10': 'Campera'
    }
    return productos.get(numero, 'Producto desconocido')

def traducir_lista_numeros_a_nombres(lista_numeros):
    return [obtener_nombre_producto(num) for num in lista_numeros]

print("Tienda de ropa online")
print("Sistema de recomendación de productos")
print("Ingresa la lista de productos que quieres comprar")
print("Catálogo disponible:")
print("1. Remera")
print("2. Pantalon")
print("3. Zapatillas")
print("4. Buzo")
print("5. Campera")
print("6. Gorra")
print("7. Guantes")
print("8. Medias")
print("9. Cinto")
print("10. Campera")

lista_usuario1 = input("\nIngrese la lista de productos del primer usuario (separados por comas, ej: 1,3,5): ").split(",")
validar_lista(lista_usuario1)
lista_usuario1 = [num.strip() for num in lista_usuario1]

lista_usuario2 = input("Ingrese la lista de productos del segundo usuario (separados por comas, ej: 2,4,6): ").split(",")
validar_lista(lista_usuario2)
lista_usuario2 = [num.strip() for num in lista_usuario2]


nombres_usuario1 = traducir_lista_numeros_a_nombres(lista_usuario1)
nombres_usuario2 = traducir_lista_numeros_a_nombres(lista_usuario2)


productos_comunes = [item for item in lista_usuario1 if item in lista_usuario2]
nombres_comunes = traducir_lista_numeros_a_nombres(productos_comunes)

productos_exclusivos_usuario1 = [item for item in lista_usuario1 if item not in lista_usuario2]
nombres_exclusivos_usuario1 = traducir_lista_numeros_a_nombres(productos_exclusivos_usuario1)

productos_exclusivos_usuario2 = [item for item in lista_usuario2 if item not in lista_usuario1]
nombres_exclusivos_usuario2 = traducir_lista_numeros_a_nombres(productos_exclusivos_usuario2)

catalogo_total = list(set(lista_usuario1 + lista_usuario2))
nombres_catalogo_total = traducir_lista_numeros_a_nombres(catalogo_total)

recomendaciones_usuario1 = nombres_exclusivos_usuario2
recomendaciones_usuario2 = nombres_exclusivos_usuario1


print("\n--- Resultados ---")
print("Lista de productos del primer usuario:", nombres_usuario1)
print("Lista de productos del segundo usuario:", nombres_usuario2)

if not nombres_comunes:
    print("\nNo hay productos en común entre los dos usuarios.")
else:
    print("\nProductos en común:", nombres_comunes)

if not nombres_exclusivos_usuario1:
    print("\nNo hay productos exclusivos del primer usuario.")
else:
    print("\nProductos exclusivos del primer usuario:", nombres_exclusivos_usuario1)

if not nombres_exclusivos_usuario2:
    print("\nNo hay productos exclusivos del segundo usuario.")
else:
    print("\nProductos exclusivos del segundo usuario:", nombres_exclusivos_usuario2)

print("\nCatálogo total:", nombres_catalogo_total)
print("\nRecomendaciones para el primer usuario:", recomendaciones_usuario1)
print("Recomendaciones para el segundo usuario:", recomendaciones_usuario2)