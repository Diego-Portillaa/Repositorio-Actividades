print('''--- Calculadora de 
             Calificación Final ---''')
#aqui ya no utilizamos los ciclos para validar reanudar una entrada de datos ya que en este caso no es necesario
# ya que el usuario puede ingresar un valor negativo y el programa lo tomara como un error y 
# le puede pedir al usuario que ingrese un valor valido
try:
    parciales = float(input("Nota de parciales (0-10): "))
    proyecto = float(input("Nota del proyecto (0-10): "))
    examen = float(input("Nota del examen (0-10): "))

    # Validamos que todas las notas estén en el rango correcto
    if 0 <= parciales <= 10 and 0 <= proyecto <= 10 and 0 <= examen <= 10:
        nota_final = (parciales * 0.40) + (proyecto * 0.30) + (examen * 0.30)
        
        if nota_final >= 6.0:
            print(f"Calificación final: {nota_final:.1f} - ¡Aprobado!")
        else:
            print(f"Calificación final: {nota_final:.1f} - Reprobado.")
    else:
        print("Error: Las calificaciones deben estar entre 0 y 10.")
#Capturamos el error de valor ingresado por el usuario y le mostramos un mensaje de error
except ValueError:
    print("Error: Por favor, ingresa solo valores numéricos.")