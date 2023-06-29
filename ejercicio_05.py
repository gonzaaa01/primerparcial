5. #Escribe un programa que calcule el sueldo de un empleado basándose en la cantidad de horas y muestre
#por pantalla el resultado, considerando lo siguiente:
#a. Si trabajo más de 120hs por mes, la hora tiene un valor de $1500.
#b. Si trabajo entre 80 y 120hs por mes, la hora tiene un valor de $1300.
#c. Si trabajo menos de 80 horas por mes, la hora tiene un valor de $1100




horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas por el empleado en el mes: "))
if horas_trabajadas  >= 120:
  sueldo = 1500

  print("El sueldo del empleado es de $" + str(sueldo))
  
horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas por el empleado en el mes: "))
if  horas_trabajadas <= 120:
  sueldo = 1300

print("El sueldo del empleado es de $" + str(sueldo))

horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas por el empleado en el mes: "))
if horas_trabajadas <= 80:
  sueldo = 1100

  print("El sueldo del empleado es de $" + str(sueldo))