4. #Escribe un programa que calcule el promedio final de una materia, basado en 3 notas de parciales,
#indicando por pantalla si el alumno aprobó o debe recursar la materia (se aprueba con 6). 






n1 = float(input("ingrese la primer nota: "))
n2 = float(input("ingrese la segunda nota: "))
n3 = float(input("ingrese la tercera nota: "))

prom = (n1+n2+n3) /3

if(prom>=6):

    print("su promedio es: ",prom,"felicitaciones, aprobo la materia")
    
else:
    print("su promedio es: ",prom,"lo lamento usted no aprobo la materia")
