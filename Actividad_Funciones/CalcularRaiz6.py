#Para este programa importaremos la biblioteca math para poder utilizar 
# la función sqrt que nos permite calcular la raíz cuadrada de un número.
import math
#Pasaremos un parámetro de entrada que será el número del cual queremos calcular su raíz cuadrada.
def calcular_raiz_cuadrada(numero):
    #Retorna la raíz cuadrada de un número no negativo.
    return math.sqrt(numero)

print("--- Calculadora de Raíz Cuadrada ---")
#Utilizamos un bloque try-except para manejar posibles errores de entrada y pedimos al usuario que ingrese un número.
try:
    valor = float(input("Ingresa un número para calcular su raíz cuadrada: "))
    #Por último, verificamos si el número es negativo y mostramos un mensaje de error
    # si lo es, de lo contrario calculamos y mostramos la raíz cuadrada.
    if valor < 0:
        print("Error: En los números reales no existe la raíz cuadrada de un valor negativo.")
    else:
        raiz = calcular_raiz_cuadrada(valor)
        print(f"La raíz cuadrada de {valor} es: {raiz:.4f}")
except ValueError:
    print("Error: Por favor, ingresa un valor numérico válido.")