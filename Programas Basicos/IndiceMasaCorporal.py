#Para esta Iteracion del programa utilizaremos 2 variables de entorno tipo Float para poder calcular 
# el indice de masa corporal de una persona sera necesario que el usuario ingrese su peso y su altura para poder hhacerlo
print('''Hola te ayudare a sacar el indice de masa corporal de una persona''')

#De igual manera que en los programas anteriores debemos someter al usuario a un bucle do-while para evitar errores
while True:
    try:
        peso=float(input("Para empezar ingrese su peso en kilogramos "))
        if peso > 0:
            break
        print("El peso debe ser mayor a 0, por favor ingresa un valor valido")
    except ValueError:
        print("Por favor ingrese un valor numerico valido para el peso")
while True:
    try:
        altura=float(input("Ahora ingrese su altura en metros "))
        if altura > 0:
            break
        print("La altura debe ser mayor a 0, por favor ingresa un valor valido")
    except ValueError:
        print("Por favor ingrese un valor numerico valido para la altura")
#Por ultimo realizamos la operacion para sacar el indice de masa corporal y lo imprimimos en pantalla
imc = peso / (altura ** 2)
#Un tip que podemos dar es que podemos utilizar :.2f  
# para que el resultado se muestre con 2 decimales y no con muchos decimales y con f string es una joya
print(f"Su indice de masa corporal es {imc:.2f}")

