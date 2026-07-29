print('''--- Números divisibles por 3 
             y 5 entre 1 y 100 ---''')
#Creamos una lista vacía para almacenar los números divisibles por 3 y 5
divisibles = []
#Recorremos los números del 1 al 100 para verificar cuáles son divisibles por 3 y 5
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        #Agregamos el número a la lista de divisibles si cumple con la condición
        divisibles.append(i)

print(f"Los números encontrados son: {divisibles}")