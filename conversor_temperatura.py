print("=== Conversor de Temperatura ===")

# Pedimos al usuario el tipo de conversión
print("Opciones:")
print("1. Celsius a Fahrenheit")
print("2. Fahrenheit a Celsius")
opcion = input("Seleccione una opción (1 o 2): ") #input imprime para escribe dato de la opcion

# Según la opción, pedimos el valor y realizamos la conversión
if opcion == "1":
    celsius = float(input("Ingrese la temperatura en Celsius: ")) # float es numeros con desimales
    fahrenheit = (celsius * 9/5) + 32  # opercion matematica para sacar los celsius
    print(f"{celsius}°C son {fahrenheit}°F")

elif opcion == "2":
    fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9 # operacion matmatica para sacr los fahrenhait
    print(f"{fahrenheit}°F son {celsius}°C")

else: 
    print("Opción no válida.")# en opciones se apreta un numero o caracter no valido