#Para esta función utilizaremos un parámetro de entrada que será la cadena de texto que queremos convertir a mayúsculas.
def convertir_a_mayusculas(cadena):
    #Devuelve la cadena ingresada convertida a mayúsculas.
    return cadena.upper()

print("--- Conversor de Texto a Mayúsculas ---")
texto = input("Ingresa una cadena de texto: ").strip()
#Y asi xualquier cadena de texto que ingrese el usuario será convertida a mayúsculas
# y mostrada en pantalla.
if texto:
    resultado = convertir_a_mayusculas(texto)
    print(f"Texto convertido: {resultado}")
else:
    print("Error: El texto no puede estar vacío.")