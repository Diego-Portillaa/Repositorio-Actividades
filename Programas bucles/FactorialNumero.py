print('''--- Calculadora 
            de Factorial ---''')
#Usamos un bloque try-except para manejar posibles errores de entrada
try:
    numero = int(input("Ingresa un número entero positivo: "))

    if numero < 0:
        print("Error: El factorial no está definido para números negativos.")
    elif numero == 0:
        print("El factorial de 0 es: 1")
    else:
        factorial = 1
        #Recorremos los números desde 1 hasta el número ingresado para calcular su factorial
        for i in range(1, numero + 1):
            factorial *= i
        print(f"El factorial de {numero} es: {factorial}")
#Cacheamos el error de valor para manejar entradas no numerales
except ValueError:
    print("Error: Por favor, ingresa un número entero válido.")