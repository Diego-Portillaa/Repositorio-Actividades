print('''--- Calculadora de Media de Positivos 
      (Ingresa un negativo para terminar) ---''')

suma = 0.0
contador = 0
#Creamos un ciclo do-while simulando un bucle infinito que se rompe con un número negativo
while True:
    #Usamos un bloque try-except para manejar posibles errores de entrada
    try:
        numero = float(input("Ingresa un número: "))

        if numero < 0:
            break  # Condición de salida

        suma += numero
        contador += 1
    #Manejamos el error de valor para entradas no numerales
    except ValueError:
        print("Error: Por favor, ingresa un número válido.\n")

if contador > 0:
    promedio = suma / contador
    print(f"\nSe ingresaron {contador} números positivos.")
    #Calculamos la media y la mostramos con dos decimales
    print(f"La media (promedio) es: {promedio:.2f}")
else:
    print("\nNo se ingresaron números positivos para calcular la media.")