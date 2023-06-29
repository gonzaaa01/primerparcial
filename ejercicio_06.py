6. #Del punto anterior, calcular y mostrar por pantalla el sueldo bruto, el monto a bonificar y el sueldo neto
#(bruto + bonif), considerando:
#a. Si trabajo más de 120hs, la bonificación es de %18
#b. Si trabajo entre 80 y 120 horas, la bonificación es de %15
#c. Si trabajo menos de 80 horas, la bonificación es de %13.






horas_trabajadas = int(input("ingrese cantidad de horas trabajadas: "))
valor_hora = float(input("ingrese el valor por hora: "))

sueldo_bruto = horas_trabajadas * valor_hora

if horas_trabajadas > 120:
    bonificacion = sueldo_bruto* 0.18

elif horas_trabajadas >= 80:
    bonificacion = sueldo_bruto * 0.15

else:
    bonificacion = sueldo_bruto * 0.13
    
    
sueldo_neto = sueldo_bruto + bonificacion

print("sueldo bruto es: ", sueldo_bruto)
print("monto a bonificar es: ", bonificacion)
print("sueldo neto es:", sueldo_neto)