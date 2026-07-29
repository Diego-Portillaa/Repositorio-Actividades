print("--- Generador de Secuencia Aritmética (do-while) ---")

try:
    inicio = float(input("Ingresa el valor inicial: "))
    paso = float(input("Ingresa la diferencia entre términos (paso): "))

    # Validación do-while para la cantidad de términos
    while True:
        terminos = int(input("¿Cuántos términos deseas generar?: "))
        if terminos > 0:
            break
        print("La cantidad de términos debe ser mayor a cero.\n")

    contador = 1
    valor_actual = inicio

    print("\nSecuencia generada:")
    # Bucle do-while para calcular y mostrar la secuencia
    while True:
        print(f"Término {contador}: {valor_actual}")
        valor_actual += paso
        contador += 1

        if contador > terminos:  # Evaluación al final del bucle
            break

except ValueError:
    print("Error: Por favor, ingresa datos numéricos válidos.")