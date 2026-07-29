print('''--- Contador de Números
      Impares (do-while) ---''')
# Bucle do-while para garantizar una entrada válida y segura del usuario
while True:
    #Usamos un bloque try-except para manejar posibles errores de entrada
    try:
        limite = int(input("Ingresa un número límite positivo: "))
        if limite > 0:
            break  #Salida del Do-While si el número es positivo
        print("Por favor, ingresa un número mayor a cero.\n")
    except ValueError:
        print("Error: Debes ingresar un entero válido.\n")

#Proceso de conteo
impares = 0
numero = 1

while True:  #Estructura do-wWhile para evaluar los números impares hasta el límite ingresado
    if numero % 2 != 0:
        impares += 1
    
    numero += 1
    
    if numero > limite:  #Condición de parada al final del ciclo
        break

print(f"Entre el 1 y el {limite} hay {impares} número(s) impar(es).")