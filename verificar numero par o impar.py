# Título
print("=== Verificador de número par o impar ===")

# Paso 1: Pedimos al usuario que escriba un número
numero = int(input("Ingrese un número entero: ")) # int  numero entero

# Paso 2: Usamos el operador % para saber si el resto es 0
if numero % 2 == 0: # if condicional  si se cumlple
    print(f"El número {numero} es PAR.")
else: # else   condicional  si no se cumple
    print(f"El número {numero} es IMPAR.")