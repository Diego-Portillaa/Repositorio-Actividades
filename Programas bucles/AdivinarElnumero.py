#Aqui usamos nuestras primeras batteries de Python
#Siendo el modulo random 
import random

print('''--- Juego: Adivina
             el Número (1 al 100) ---''')
#Establecemos un número secreto aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)
intentos = 0
adivinado = False
#Sometemos el bloque de código a un bucle while 
# que se ejecutará hasta que el usuario adivine el número
while not adivinado:
    #Usamos un bloque try-except para manejar posibles errores de entrada
    try:
        intento = int(input("Ingresa tu número (1-100): "))
        intentos += 1
        #Se abre un bloque condicional para verificar si el número ingresado es valido 
        if intento < 1 or intento > 100:
            print("Por favor, ingresa un número dentro del rango (1 a 100).\n")
        elif intento < numero_secreto:
            print("El número secreto es MAYOR. Intenta de nuevo.\n")
        elif intento > numero_secreto:
            print("El número secreto es MENOR. Intenta de nuevo.\n")
        else:
            adivinado = True
            print(f"\n¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intento(s).")
    #Manejamos el error de valor para entradas no numerales
    except ValueError:
        print("Error: Ingresa un número entero válido.\n")