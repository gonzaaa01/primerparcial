10. #Escribe un programa que calcule el promedio general de una clase.





estudiante = int(input("cantidad de alumnos a ingresar: "))
suma_general = 0
contador = 0

while contador < estudiante:
    notas = float(input("ingrese nota del alumno: "))
    suma_general += notas
    contador = contador +1

promedio = suma_general / estudiante
print("el promedio de la clase es: ",(promedio))