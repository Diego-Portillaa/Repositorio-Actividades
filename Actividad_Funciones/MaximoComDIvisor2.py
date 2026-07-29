#Creamos una función para calcular el Máximo Común Divisor (MCD)
# de dos números enteros utilizando el algoritmo de Euclides:)
def calcular_mcd(a, b):
    #Calcula el Máximo Común Divisor utilizando el algoritmo de Euclides.
    #Abrimos un bucle que continuará hasta que b sea igual a 0, moment
    # o en el cual a contendrá el MCD.
    while b != 0:
        a, b = b, a % b
    return abs(a)

print("--- Calculadora de Máximo Común Divisor (MCD) ---")
#Por último, pedimos al usuario que ingrese dos números y usamos 
# la función para calcular su MCD.
try:
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    
    resultado = calcular_mcd(num1, num2)
    print(f"El MCD entre {num1} y {num2} es: {resultado}")
except ValueError:
    print("Error: Debes ingresar números enteros válidos.")