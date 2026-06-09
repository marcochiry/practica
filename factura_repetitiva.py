print("===================================")
print("BIENVENIDOS AL SISTEMA DE COMPRAS")
print("===================================")

#Vamos a crear una variable que controla la ejecución del menú
ejecutando = True

#Variables para acumalar
total_ventas = 0
cantidad_compras = 0


while ejecutando:
    print()


#Entradas de datos
cliente = input("Ingrese el nombre del cliente: ")
producto = input("Ingrese el nombre del producto: ")

#Entrada de datos con numeros que tienen decimales
precio = float(input("Ingrese el precio del producto: "))

#Entrada de datos con numeros enteros
cantidad = int(input("Ingrese la cantidad del producto: "))

#Verificar si el precio es valido (mayor a 0)
if precio <= 0:
    print("ERROR: El precio debe ser mayor a 0.")

#Verificar si la cantidad es valida (mayor a 0)
if cantidad <= 0:
    print("ERROR: La cantidad debe ser mayor a 0.")

#Calculo del subtotal
subtotal = precio * cantidad

#Iniciar el impuesto al 13%
impuesto = subtotal * 0.13

descuento = 0

#Si compramos más de 10 productos, tenemos 5% de descuento
if cantidad >= 10:
    descuento = subtotal * 0.05
    print("¡Felicidades! Has obtenido un descuento del 5% por comprar más de 10 productos.")

#Si pagamos más de 100.000 colones tenemos un descuento del 10%
if subtotal >= 100000:
    descuento += subtotal * 0.10
    print("¡Felicidades! Has obtenido un descuento del 10% por pagar más de 100.000 colones.")

#Calculo del total a pagar
total = subtotal + impuesto - descuento

#Salida de datos (factura)

print("\n================FACTURA===================")

print("Cliente: ", cliente)

print("Producto: ", producto)

print("Precio unitario: ", precio)

print("Cantidad de productos: ", cantidad)

print("Subtotal: ", subtotal)

print("Impuesto del 13%: ", impuesto)

print("El descuento es de: ", descuento)

print("------------------------------------------")

print("Total a pagar: ", total)

#Mensaje de ganancias

if total >=20000:
    print("Felicidades te ganastes un capucchino gratis")
elif total >= 10000:
    print("Felicidades te ganastes un café negro grande gratis")
else:
    print("Felicidades te ganastes un café negro pequeño gratis")