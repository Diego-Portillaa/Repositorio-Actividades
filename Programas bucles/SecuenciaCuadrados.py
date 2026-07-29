print('''--- Secuencia de Cuadrados (do-while) ---''')

#Validación do-while para asegurar que el usuario ingrese un número positivo
while True:
    #Como siempre manejamos posibles errores de entrada con un bloque try-except
    try:
        n = int(input("¿Hasta qué número deseas generar la secuencia de cuadrados?: "))
        if n > 0:
            break
        print("Por favor, ingresa un número entero positivo.\n")
    except ValueError:
        print("Error: Ingresa un número entero válido.\n")

i = 1
print(f"\nCuadrados del 1 al {n}:")

# Bucle do-while para imprimir la secuencia
while True:
    cuadrado = i ** 2
    #Iteramos desde 1 hasta n, calculando el cuadrado de cada número y mostrándolo
    print(f"{i}² = {cuadrado}")
    
    i += 1
    
    if i > n:  # Condición al final del bucle
        break