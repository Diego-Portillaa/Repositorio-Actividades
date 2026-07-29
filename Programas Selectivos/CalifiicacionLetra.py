print('''--- Conversor de 
             Calificación a Letra ---''')
#De igual manera podemos evitar el uso de ciclos para validar 
# la entrada de datos ya que en este caso no es necesario
#Utilizamos un try-except para capturar posibles errores
# de entrada de datos y mostrar un mensaje de error al usuario
try:
    puntaje = float(input("Ingresa tu puntaje (0-100): "))

    if puntaje < 0 or puntaje > 100:
        print("Error: El puntaje debe estar entre 0 y 100.")
    elif puntaje >= 90:
        print("Tu calificación es: A (Excelente)")
    elif puntaje >= 80:
        print("Tu calificación es: B (Buena)")
    elif puntaje >= 70:
        print("Tu calificación es: C (Aceptable)")
    elif puntaje >= 60:
        print("Tu calificación es: D (Suficiente)")
    else:
        print("Tu calificación es: F (Insuficiente)")
#Cachamos posibles errores de entrada de datos y mostramos
# un mensaje de error al usuario
except ValueError:
    print("Error: Por favor, ingresa solo números.")