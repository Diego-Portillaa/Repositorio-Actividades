print('''- Calculadora de
      Descuentos - ''')
#Aqui ya no utilizamos los ciclos para validar reanudar una entrada de
# datos ya que en este caso no es necesario 
# ya que el usuario puede ingresar un valor negativo y el programa
# lo tomara como un error y le pedira al usuario que ingrese un valor valido
try:
    monto = float(input("Ingresa el monto total de la compra: $"))
    if monto <= 0:
        print("Error: El monto debe ser un valor positivo.")
    elif monto <= 100:
        porcentaje = 0
    elif monto <= 200:
        porcentaje = 5
    elif monto <= 500:
        porcentaje = 10
    else:
        porcentaje = 15
#Operamos el valor y lo redondeamos a 2 decimales para que el resultado sea
# mas legible y no tenga muchos decimales
    if monto > 0:
        descuento = monto * (porcentaje / 100)
        total = monto - descuento
        print(f"Descuento aplicado ({porcentaje}%): ${descuento:.2f}")
        print(f"Total a pagar: ${total:.2f}")
#Podemos cachear posibles errores de entrada de datos y mostrar un 
# mensaje de error al usuario
except ValueError:
    print("Error: Por favor, ingresa un valor numérico válido.")