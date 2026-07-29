#Para este codigo utilizaremos 3 variables de entorno tipo Float para poder calcular el salario neto de una persona 
# sera necesario que el usuario ingrese su salario bruto y su porcentaje de 
# descuento impuestos y deducciones para poder hacerlo
print('''Hola te ayudare a 
      calcular tu salario neto individual''')
while True:
    try:
        salario_bruto=float(input("Para empezar ingrese su salario bruto porfavor"))
        if salario_bruto > 0:
            break
        print("El salario bruto debe ser mayor a 0, por favor ingresa un valor valido")
    except ValueError:
        print("Por favor ingrese un valor numerico valido para el salario bruto")
while True:
    try:
        porcentaje_impuestos=float(input("Ahora ingrese el porcentaje de impuestos que se le descuenta de nomina"))
        if porcentaje_impuestos > 0:
            break
        print("El porcentaje de impuestos debe ser mayor a 0, por favor ingresa un valor valido")
    except ValueError:
        print("Por favor ingrese un valor numerico valido para el porcentaje de impuestos")
while True:
    try:
        porcentaje_deducciones=float(input("Por ultimo ingrese el porcentaje de deducciones que se le descuenta del infonavit"))
        if porcentaje_deducciones > 0:
            break
        print("El porcentaje de deducciones debe ser mayor a 0, por favor ingresa un valor valido")
    except ValueError:
        print("Por favor ingrese un valor numerico valido para el porcentaje de deducciones")
# Por ultimo realizamos la operacion para sacar el salario neto y lo imprimimos en pantalla(hacemos una regla de tres)
salario_neto = salario_bruto - (salario_bruto * (porcentaje_impuestos / 100)) - (salario_bruto * (porcentaje_deducciones / 100))
print(f"Su salario neto es {salario_neto}")
