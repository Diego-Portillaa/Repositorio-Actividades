#Programa para invertir el orden de los elementos de una lista
#Primero declaramos una función que reciba una lista como parámetro
# y luego retorne la lista invertida utilizando slicing.
def invertir_lista(lista):
    #Retornamos la lista invertida usando slicing
    return lista[::-1]

print("--- Invertir Elementos de una Lista ---")
entrada = input("Ingresa los elementos de la lista separados por espacios: ").strip()
#Nos aseguramos de que el usuario haya ingresado al menos un element
# o antes de llamar a la función para invertir la lista y mostrar los resultados.
if not entrada:
    print("Error: No ingresaste ningún elemento.")
else:
    elementos = entrada.split()
    lista_invertida = invertir_lista(elementos)

    print(f"\nLista original: {elementos}")
    print(f"Lista invertida: {lista_invertida}")