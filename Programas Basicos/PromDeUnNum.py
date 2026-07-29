#Para este programa utilizaremos 3 variables de entorno tipo Float
print('''Hola te ayudare a sacar el 
            promedio de 3 numeros ''')
#De igual manera que en el programa anterior debemos someter al usuario a un bucle do-while para evitar errores
while True:
    try:
        num1=float(input("Para empezar ingrese el primer numerito "))
        if num1 > 0:
            break
        print("El numero debe ser mayor a 0, por favor ingresa un valor valido")
    except ValueError:
        print("Por favor ingrese un valor numerico valido para el primer numero")
while True:
    try:
        num2=float(input("Ahora ingrese el segundo numerito "))
        if num2 > 0:
            break
        print("El numero debe ser mayor a 0, por favor ingresa un valor valido")
    except ValueError:
        print("Por favor ingrese un valor numerico valido para el segundo numero")
while True:
    try:
        num3=float(input("Por ultimo ingrese el tercer numerito "))
        if num3 > 0:
            break
        print("El numero debe ser mayor a 0, por favor ingresa un valor valido")
    except ValueError:
        print("Por favor ingrese un valor numerico valido para el tercer numero")

# Por ultimo realizamos la operacion para sacar el promedio de los 3 numeros
# y lo imprimimos en pantalla es importante que sea con / y no con // ya que de lo contrario el resultado 
# seria un numero entero y no un numero decimal
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los 3 numeros es {promedio}")