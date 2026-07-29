#Programa para contar números pares e impares en una lista
#Primero recorremos con el metodo for cada elemento de la lista y verificamos si es par o impar utilizando el operador módulo (%).
def contar_pares_impares(lista):
    pares = 0
    impares = 0
    for num in lista:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    #Devolvemos la cantidad de números pares e impares encontrados en la lista.
    return pares, impares

print("--- Contador de Pares e Impares en una Lista ---")
#Despues pedimos al usuario que ingrese una lista de números enteros separados por espacios y manejamos posibles errores de entrada.
try:
    entrada = input("Ingresa números enteros separados por espacios: ")
    #Convertimos la cadena ingresada en una lista de enteros
    numeros = [int(x) for x in entrada.split()]
    #Por último, verificamos si la lista está vacía y mostramos un mensaje de error si lo está, 
    # si no llamamos a la función para contar los números pares e impares y mostramos los resultados.
    if not numeros:
        print("Error: La lista no puede estar vacía.")
    else:
        total_pares, total_impares = contar_pares_impares(numeros)
        print(f"\nLista analizada: {numeros}")
        print(f"Cantidad de pares: {total_pares}")
        print(f"Cantidad de impares: {total_impares}")
#Manejamos la excepción ValueError en caso de que el usuario ingrese valores no enteros.
except ValueError:
    print("Error: Asegúrate de ingresar únicamente números enteros.")