#Programa para calcular la suma de todos los elementos de una lista
#Aqui tambien primero definimos una función que reciba una lista como parámetro y
# luego este mismo recorra cada elemento de la lista sumándolos a una variable acumuladora.
def sumar_elementos(lista):
    suma_total = 0
    for elemento in lista:
        suma_total += elemento
    #Devolvemos la suma total de los elementos de la lista.
    return suma_total

print("--- Suma de Elementos de una Lista ---")
#Utilizamos un bloque try-except para manejar posibles errores de entrada
# y pedimos al usuario que ingrese una lista de números separados por espacios
try:
    entrada = input("Ingresa números (pueden ser decimales) separados por espacios: ")
    numeros = [float(x) for x in entrada.split()]
     #Por ultimo, verificamos si la lista está vacía y mostramos un mensaje de error si lo está, 
    # si no llamamos a la función para sumar los elementos de la lista y mostramos el resultado
    if not numeros:
        print("Error: Debes ingresar al menos un número.")
    else:
        resultado = sumar_elementos(numeros)
        print(f"\nLista ingresada: {numeros}")
        print(f"La suma total de los elementos es: {resultado}")
#manejamos la excepción ValueError en caso de que el usuario ingrese valores no numéricos.
except ValueError:
    print("Error: Ingresa valores numéricos válidos.")