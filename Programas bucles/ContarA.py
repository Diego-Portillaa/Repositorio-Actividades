print('''--- Contador de
      Letras 'A' ---''')

texto = input("Ingresa una palabra o frase: ").strip()
#Manejamos el caso en que el usuario no ingrese ningún texto
if texto == "":
    print("Error: No ingresaste ningún texto.")
else:
    contador = 0
    #Bajamos el texto para contar 'A', 'a', 'Á' y 'á'
    texto_limpio = texto.lower()
    #Recorremos cada caracter del texto ingresado para 
    # contar las apariciones de "a"
    for caracter in texto_limpio:
        if caracter in ('a', 'á'):
            contador += 1

    print(f"La letra 'a' aparece {contador} veces en el texto ingresado.")