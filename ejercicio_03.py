3. #Escribe un programa que calcule la equivalencia a pesos de los dólares ingresados por pantalla. El
#programa debe preguntar el tipo de cambio a convertir (es decir, cuánto cotiza el dólar).





tipo_cambio = float(input("ingrese el tipo de cambio actual: "))

dolar = float(input("ingrese la cantidad en dolar a convertir: "))
peso = dolar*tipo_cambio

print(f"{dolar} dolares equivalen a {peso} pesos.")