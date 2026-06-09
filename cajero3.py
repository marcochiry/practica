def cajero_automatico():
    #variables q se van a ocupar
    saldo = 1000  # Saldo inicial
    historial_pin_incorrectos = []
    historial_transacciones = []
    fondos_insuficientes = 0
# menu pricipal de inicio
    while True:
        print("Menú Principal:")
        print("(1) Iniciar sesión  (2) Salir")
        opcion = input("Seleccione una opción: ")
#ingreso de pin de tarjeta y intetos
        if opcion == "1":
            intentos = 0
            pin = ""
            while intentos < 3 and pin != "1234":
                pin = input("Ingrese su PIN: ")
                if pin == "1234":
                    print("PIN correcto. Accediendo a operaciones...")
                else:
                    historial_pin_incorrectos.append(pin) # ( .append  es agregar a una lista de trassaciones  en este caso (pin incorrecto))
                    print("PIN incorrecto. Intento {intentos + 1} de 3.")
                intentos += 1
#menu segundario
            if pin == "1234":
                en_sesion = True
                while en_sesion:
                    print("Menú de Operaciones:")
                    print("(1) Consultar saldo")
                    print("(2) Depositar dinero")
                    print("(3) Retirar dinero")
                    print("(4) Ver historial")
                    print("(5) Cerrar sesión")
                    opcion = input("Seleccione una opción: ")
#historial de trasaciones
                    if opcion == "1":
                        print(f"Saldo actual: {saldo}")
                        historial_transacciones.append({"operación": "consulta", "saldo": saldo})
                    
                    elif opcion == "2":
                        try:
                            monto = float(input("Ingrese el monto a depositar: "))
                            if monto > 0:
                                saldo += monto # suma el munto del saldo mas el munto depocitado
                                print(f"Depósito realizado. Nuevo saldo: {saldo}")
                                historial_transacciones.append({"operación": "depósito", "monto": monto, "nuevo saldo": saldo})
                            else:
                                print("Monto no válido. Intente nuevamente.")
                        except:
                            print("Entrada inválida.")
                    
                    elif opcion == "3":
                        try:
                            monto = float(input("Ingrese el monto a retirar: "))
                            if 0 < monto <= saldo:
                                saldo -= monto
                                print(f"Retiro realizado. Nuevo saldo: {saldo}")
                                historial_transacciones.append({"operación": "retiro", "monto": monto, "nuevo saldo": saldo})
                            else:
                                fondos_insuficientes += 1
                                print("Saldo insuficiente o monto inválido.")
                                historial_transacciones.append({"operación": "fallo retiro", "monto": monto, "saldo actual": saldo})
                        except:
                            print("Entrada inválida.")
                    
                    elif opcion == "4":
                        print("Historial de transacciones:")
                        for transaccion in historial_transacciones:
                            print(transaccion)
                        print("PIN incorrectos ingresados: {historial_pin_incorrectos}")
                        print("Veces con fondos insuficientes: {fondos_insuficientes}")
                    
                    elif opcion == "5":
                        print("Cerrando sesión...")
                        en_sesion = False # independientemente si la occion es falsa o verdadera te regresa al menu principal.
                    else:
                        print("Opción no válida. Intente de nuevo.")# no exite el numero ingresado menu segundario
            else:
                print("Cuenta bloqueada por máximos intentos fallidos.")
                break  # Termina el programa por maximo de intentos incorrectos

        elif opcion == "2":
            print("Gracias por usar el cajero automático. Hasta luego.")
            break  # Termina el programa menu principal

        else:
            print("Opción no válida. Intente nuevamente.") # no exite mumero menu primario

# Ejecutar el programa
cajero_automatico()