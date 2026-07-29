#Para la creacion de este programa utilizaremos 2 variables de entorno tipo Float

print('''Hola te ayudare a sacar el area de un
                     rectangulo''')
#Para asegurar que el programa se ejecute correctamente 
#debemos someter al usuario a un bucle do-while para evitar errores 
#desde el principio ya que el usuario no tiene el mismo conocimiento del programa
#que nosotros

while True:
    #Utilizamos un try-except para evitar que el programa se crashe
    #en caso de que el usuario ingrese un valor no valido es muy comodo
    try:
        altura=float(input("Para empezar ingrese la altura de dicha figura "))
        #aqui rompemos el bucle si el numero es mayor a 0
        if altura > 0:
            break
        print("La altura debe ser mayor a 0, por favor ingresa un valor valido")
    except ValueError:
        print("Por favor ingrese un valor numerico valido para la altura")
while True:
    try:
        base=float(input("Ahora dame la base de dicho rectangulo "))
        #De igual manera rompemos el bucle si el numero es mayor a 0
        if base > 0:
            break
        print("La base debe ser mayor a 0, por favor ingresa un valor valido")
    except ValueError:
        print("Por favor ingrese un valor numerico valido para la base")
#Por ultimo realizamos la operacion para sacar el area del rectangulo y la podemos imprimir en pantalla
resultado =altura * base
print(f"El area del rectangulo es {resultado}")

