
print('''--- Calculadora 
      Básica con Menú ---''')

#Ciclo do-while simulado para mostrar el menú hasta que el usuario decida salir
while True:
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Selecciona una opción (1-5): ").strip()
    #Rompemos el bucle si el usuario selecciona la opción de salir
    if opcion == "5":
        print("¡Hasta luego!")
        break

    if opcion in ("1", "2", "3", "4"):
        #Usamos un bloque try-except para manejar posibles errores de entrada
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            #Utilizamos un bloque match-case para manejar las operaciones
            # según la opción seleccionada de una manera mas sencilla
            match opcion:
                case "1":
                    print(f"Resultado: {num1} + {num2} = {num1 + num2}")
                case "2":
                    print(f"Resultado: {num1} - {num2} = {num1 - num2}")
                case "3":
                    print(f"Resultado: {num1} * {num2} = {num1 * num2}")
                case "4":
                    if num2 != 0:
                        print(f"Resultado: {num1} / {num2} = {num1 / num2}")
                    else:
                        print("Error: No se puede dividir entre cero.")
        #Manejamos el error de valor para entradas no numerales
        except ValueError:
            print("Error: Por favor, ingresa solo valores numéricos.")
    else:
        print("Opción no válida. Inténtalo de nuevo.")