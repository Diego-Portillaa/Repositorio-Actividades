print('''--- Contador de Números
      (Positivos, Negativos, Ceros) ---''')
#Usamos un bloque try-except para manejar posibles errores de entrada
try:
    total_numeros = int(input("¿Cuántos números deseas ingresar?: "))

    if total_numeros <= 0:
        print("Error: Debes ingresar al menos un número para evaluar.")
    else:
        mayores = 0
        menores = 0
        iguales = 0
        #Recorremos la cantidad de números que el usuario desea ingresar
        for i in range(total_numeros):
            num = float(input(f"Ingresa el número {i + 1}: "))
            if num > 0:
                mayores += 1
            elif num < 0:
                menores += 1
            else:
                iguales += 1

        print("\n--- Resultados ---")
        print(f"Mayores a cero (positivos): {mayores}")
        print(f"Menores a cero (negativos): {menores}")
        print(f"Iguales a cero: {iguales}")
#Cacheamos el error de valor para manejar entradas no numerales 
except ValueError:
    print("Error: Debes ingresar un valor numérico válido.")