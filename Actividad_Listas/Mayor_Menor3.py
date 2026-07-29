#Programa para hayar el valor mayor y menor en una lista

#También definimos una función que reciba una lista como parámetro y luego 
# recorra cada elemento de la lista para determinar cuál es el mayor y cuál es el menor.
def obtener_mayor_y_menor(lista):
    #Como primer paso, inicializamos las variables mayor y
    # menor con el primer elemento de la lista.
    mayor = lista[0]
    menor = lista[0]
    #Iteramos a través de la lista desde el segundo elemento hasta el final 
    # para comparar cada número con las variables mayor y menor.
    for num in lista[1:]:
        if num > mayor:
            mayor = num
        if num < menor:
            menor = num
    #devolvemos una tupla con el valor mayor y menor encontrados en la lista.
    return mayor, menor

print("--- Búsqueda de Valor Mayor y Menor ---")
#Hacemos un bloque try-except para manejar posibles errores de entrada y pedimos al usuario que ingrese una lista de números separados por espacios.
try:
    entrada = input("Ingresa números separados por espacios: ")
    numeros = [float(x) for x in entrada.split()]
    #Por último, verificamos si la lista está vacía y mostramos un mensaje de error si lo está, 
    # si no llamamos a la función para obtener el mayor y menor de la lista y mostramos los resultados
    if not numeros:
        print("Error: No se ingresaron elementos.")
    else:
        maximo, minimo = obtener_mayor_y_menor(numeros)
        print(f"\nLista de números: {numeros}")
        print(f"El número MAYOR es: {maximo}")
        print(f"El número MENOR es: {minimo}")
#Manejamos la excepción ValueError en caso de que el usuario ingrese valores no numéricos.
except ValueError:
    print("Error: Por favor, ingresa solo valores numéricos.")