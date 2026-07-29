print('''--- Determinador de Estación del Año ---''')
#Aqui utilizamos .strip para eliminar espacios en blanco 
# al inicio y al final de la cadena
mes = input("Ingresa el nombre del mes: ").strip().lower()
#Match case es una estructura de control parecida 
#a un switch case en otros lenguajes de programación, o a un if-elif-else, que 
# es mucho mas tedioso de escribir y leer, por lo que match case es mejor
match mes:
    case "marzo" | "abril" | "mayo":
        estacion = "Primavera"
    case "junio" | "julio" | "agosto":
        estacion = "Verano"
    case "septiembre" | "octubre" | "noviembre":
        estacion = "Otoño"
    case "diciembre" | "enero" | "febrero":
        estacion = "Invierno"
    case _:
        estacion = None
#Por ultimo utilizamos capitalize para poner la primera letra del mes en mayuscula
# y el resto en minuscula
if estacion:
    print(f"El mes de {mes.capitalize()} pertenece a la estación: {estacion}")
else:
    print("Error: Por favor, ingresa un mes válido.")