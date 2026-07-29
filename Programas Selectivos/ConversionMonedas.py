print('''--- Conversor de 
      Pesos Mexicanos (MXN) ---''')
#Aqui TAMBIEN podemos utilizar un try-except para capturar posibles errores de entrada de datos y 
# mostrar un mensaje de error al usuario
try:
    monto_mxn = float(input("Ingresa el monto en pesos mexicanos (MXN): $"))
    
    if monto_mxn <= 0:
        print("Error: El monto debe ser mayor a cero.")
    else:
        print("Monedas disponibles: USD, EUR, THB, JPY, KRW, AUD, PEN, CAD, VES, ARS")
        moneda = input("¿A qué moneda deseas convertir?: ").strip().upper()

        match moneda:
            case "USD":
                tasa = 0.055  # Dólar estadounidense
            case "EUR":
                tasa = 0.050  # Euro
            case "THB":
                tasa = 1.95   # Baht tailandés
            case "JPY":
                tasa = 8.50   # Yen japonés
            case "KRW":
                tasa = 75.0   # Won surcoreano
            case "AUD":
                tasa = 0.083  # Dólar australiano
            case "PEN":
                tasa = 0.20   # Sol peruano
            case "CAD":
                tasa = 0.075  # Dólar canadiense
            case "VES":
                tasa = 2.00   # Bolívar venezolano
            case "ARS":
                tasa = 50.0   # Peso argentino
            case _:
                tasa = None
        #Cuando la tasa sea aceptada, 
        # operamos el valor y lo redondeamos a 2 decimales
        if tasa:
            total = monto_mxn * tasa
            print(f"\n${monto_mxn:.2f} MXN equivalen a {total:.2f} {moneda}")
        else:
            print("Error: Moneda no soportada.")
#Cachamos posibles errores de entrada de datos y mostramos un mensaje de error al usuario   
except ValueError:
    print("Error: Ingresa un valor numérico válido.")