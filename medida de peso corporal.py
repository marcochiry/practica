print("=== Calculadora de peso corporal ===")

# Paso 1: Pedimos al usuario su peso y altura
peso = float(input("Ingrese su peso en kilogramos (kg): "))
altura = float(input("Ingrese su altura en metros (m): "))

# Paso 2: Calculamos el IMC usando la fórmula
imc = peso / (altura ** 2)

# Paso 3: Mostramos el resultado con 2 decimales
print(f"Tu IMC es: {imc:.2f}") # imc     muestra el numero con 2 decimales

# Paso 4: Interpretamos el resultado
if imc < 18.5:
    print("Clasificación: Bajo peso")
elif imc < 25:
    print("Clasificación: Peso saludable")
elif imc < 30:
    print("Clasificación: Sobrepeso")
else:
    print("Clasificación: Obesidad")