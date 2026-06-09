while True:
    # Suma, resta, multiplicación y división
    num1 = float(input("Primer número: ")) #float numeros decimales   input    pedirle algo al usuario
    operacion = input("Operación (+, -, *, /,^): ") # pedir q operacion ocupa
    num2 = float(input("Segundo número: ")) # pide segundo numero

    if operacion == '+':  # if es SI es igual a +
        resultado= num1 + num2 # se suma num1 + num2 y se ase variable RESULTADO
    elif operacion == '-':
        resultado= num1 - num2
    elif operacion == '*':
        resultado = num1 * num2
    elif operacion == '/':
        if num2 != 0:  # Evita que el programa falle si dividen entre cero
            resultado =num1 / num2
        else:
            resultado ="error  no se puede dividir entre cero"
    elif operacion == '^':
        resultado =num1 ** num2
    else:
        print("Operación no válida")
        resultado = None   # indicate invalid

    if resultado is not None:
        print( " el resultado es :" , resultado) # tiene que ponerle la coma para imprimir la variable y salga el numero
    # Pregunta sencilla para terminar el bucle
    continuar = input("¿Quieres hacer otra operación? (si/no): ")
    if continuar == 'no':
        print("¡Adiós!")
        break # Break the loop and end the program