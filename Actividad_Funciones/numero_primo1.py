#Para esta Actividad usaremos una función que nos permita determinar si un número es primo o no. Un número primo 
# es aquel que solo es divisible por 1 y por sí mismo, y debe ser mayor que 1,etc.
def es_primo(numero):
    #Retorna True si el número es primo, False en caso contrario.
    if numero <= 1:
        return False
    #Iteramos desde 2 hasta la raíz cuadrada del número para verificar si tiene divisores
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

print("--- Verificador de Números Primos ---")
#Por ultimo, pedimos al usuario que ingrese un número y usamos la función para determinar si es primo o no.
try:
    num = int(input("Ingresa un número entero positivo: "))
    if num < 0:
        print("Error: Ingresa un entero mayor o igual a cero.")
    elif es_primo(num):
        print(f"El número {num} SÍ es un número primo.")
    else:
        print(f"El número {num} NO es un número primo.")
#Manejamos el error de valor para entradas no numerales
except ValueError:
    print("Error: Por favor, ingresa un número entero válido.")