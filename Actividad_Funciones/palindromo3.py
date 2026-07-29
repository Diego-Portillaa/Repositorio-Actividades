#Para esta funcion utilizaremos un parámetro de entrada que será la cadena de
# texto que queremos evaluar si es un palíndromo o no. 
# Un palíndromo es como una palabra o frase que se lee igual hacia adelante y hacia atrás,
def es_palindromo(texto):
    #Retorna True si la cadena de texto es un palíndromo.
    # Limpiamos el texto: quitamos espacios y convertimos a minúsculas
    limpio = "".join(caracter.lower() for caracter in texto if caracter.isalnum())
    return limpio == limpio[::-1]

print("--- Verificador de Palíndromos ---")
entrada = input("Ingresa una palabra o frase: ").strip()
#Por último, verificamos si la entrada es un palíndromo y mostramos el resultado al usuario.
if not entrada:
    print("Error: No ingresaste ningún texto.")
elif es_palindromo(entrada):
    print(f'"{entrada}" SÍ es un palíndromo.')
else:
    print(f'"{entrada}" NO es un palíndromo.')