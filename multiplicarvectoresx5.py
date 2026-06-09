# Inicializamos la multiplicar en 1.solo multiplicar
numeros = []
rest=1
# Repetimos 5 veces para pedir los números
for i in range(5):
    num = int(input(f"Ingrese el número : "))
    numeros.append(num)

for i in range (5) :
    rest*= numeros[i]

# Mostramos el resultado
print(f"La suma total es: {rest}")