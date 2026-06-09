import time  # Importamos el módulo para trabajar con tiempo

print("=== Contador regresivo ===")

# Paso 1: Pedir al usuario desde qué número quiere comenzar
inicio = int(input("Ingrese el número para comenzar el conteo regresivo: "))

# Paso 2: Usamos un bucle while que cuenta hacia atrás
while inicio > 0:
    print(inicio)
    time.sleep(1)  # Espera 1 segundo antes de seguir
    inicio -= 1    # Resta 1 al número

# Paso 3: Cuando termina el conteo
print("¡Tiempo terminado! 🎉")