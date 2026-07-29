print('''--- Contador
             de Dígitos ---''')
#Manejamos posibles errores de entrada con un bloque try-except
try:
    numero = int(input("Ingresa un número entero: "))
    
    # Aqui podemos trabajar con el valor absoluto para
    # manejar números negativos
    num_abs = abs(numero)
    
    # Importante convertir a string para contar la cantidad de dígitos
    cantidad_digitos = len(str(num_abs))

    print(f"El número {numero} tiene {cantidad_digitos} dígito(s).")

except ValueError:
    print("Error: Por favor, ingresa un número entero válido.")