#Para esta función utilizaremos tres parámetros de entrada: la cadena de texto original,
# el carácter que queremos buscar y el carácter con el que queremos reemplazarlo.
def reemplazar_caracter(cadena, buscar, nuevo):
    #Reemplaza todas las ocurrencias de 'buscar' por 'nuevo' dentro de 'cadena'.
    return cadena.replace(buscar, nuevo)

print("--- Reemplazador de Caracteres ---")
texto = input("Ingressa el texto original: ")
#Por último, pedimos al usuario que ingrese el carácter a buscar y
# el carácter de reemplazo, y mostramos el resultado final.
if texto:
    caracter_original = input("Ingresa el carácter a buscar: ")
    caracter_nuevo = input("Ingresa el carácter de reemplazo: ")

    if len(caracter_original) == 1 and len(caracter_nuevo) == 1:
        resultado = reemplazar_caracter(texto, caracter_original, caracter_nuevo)
        print(f"Resultado final: {resultado}")
    else:
        print("Error: Debes ingresar exactamente un único carácter para buscar y reemplazar.")
else:
    print("Error: El texto inicial no puede estar vacío.")