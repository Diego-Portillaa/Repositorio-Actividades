print('''--- Verificación
      para Votar ---''')
#De igual manera podemos evitar el uso de ciclos para validar 
# la entrada de datos ya que en este caso no es necesario
#Utilizamos un try-except para capturar posibles errores
# de entrada de datos y mostrar un
try:
    edad = int(input("Ingresa tu edad: "))

    if edad < 0:
        print("Error: La edad no puede ser negativa.")
    elif edad >= 18:
        print("Puedes votar. Cumples con la mayoría de edad.")
    else:
        #Aqui como extra podemos agregar un mensaje al usuario que le indique
        # cuantos años le faltan para poder votar
        faltan = 18 - edad
        print(f"No puedes votar. Te faltan {faltan} años para cumplir 18.")
#Cachamos posibles errores de entrada de datos y mostramos un mensaje 
# de error al usuario
except ValueError:
    print("Error: Por favor, ingresa un número entero válido.")