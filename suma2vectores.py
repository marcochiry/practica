# Inicializamos la suma en 0
numeros = []
numeros2 = []
rest=0
# Repetimos 5 veces para pedir los números 
for i in range(5):
    num = int(input(f"Ingrese el número vecto 1 : "))
    numeros.append(num)
    # Repetimos 5 veces para pedir los números segundo vector
for i in range(5):
    num2 = int(input(f"Ingrese el número vector 2 : "))
    numeros2.append(num2)
    # vacior vectores con la suma
for i in range (5) :
    rest+= numeros[i] + numeros2 [i]
# Mostramos el resultado
print(f"La suma total de vectores eses: {rest}")
