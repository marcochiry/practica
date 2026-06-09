nombre = input("Nombre del estudiante: ")
edad = int(input("Edad del estudiante: "))
carrera = input("carrera que crusa: ")

nota1 = float(input("Nota del primer examen: "))
nota2 = float(input("Nota del segundo examen: "))

suma = nota1 + nota2
promedio = suma / 2
diferencia = nota1 - nota2
print("===== RESULTADOS =====")
print("Nombre:", nombre)
print("Edad:", edad)
print("Carrera:", carrera)
print("Suma de notas:", suma)
print("Promedio:", promedio)
print("Diferencia:", diferencia)

if promedio >= 70:
    print("El estudiante aprobó el curso")
if promedio >= 70:
    print("Aprobado")
else:
    print("Reprobado")
if edad >= 18 and promedio >= 80:
    print("Puede aplicar a beca académica")
if nota1 < 50 or nota2 < 50:
    print("Debe mejorar su rendimiento académico")