print('''--- Conversor de 
            Grados Celsius ---''')
#Aqui si podemos utilizar un try-except para capturar 
# posibles errores de entrada de datos y mostrar un mensaje de error al usuario
try:
    celsius = float(input("Ingresa la temperatura en °C: "))
    print("Opciones de conversión:\n1. Fahrenheit\n2. Kelvin")
    opcion = input("Selecciona la opción (1 o 2): ").strip()

    match opcion:
        case "1" | "fahrenheit":
            resultado = (celsius * 9/5) + 32
            #Utilizamos .2f para redondear el resultado a 2 decimales y que sea mas legible
            print(f"{celsius}°C equivalen a {resultado:.2f}°F")
        case "2" | "kelvin":
            resultado = celsius + 273.15
            print(f"{celsius}°C equivalen a {resultado:.2f} K")
        case _:
            print("Error: Opción de conversión no válida.")
#Cachamos posibles errores de entrada de datos y mostramos un mensaje de error al usuario
except ValueError:
    print("Error: Debes ingresar un número válido para la temperatura.")