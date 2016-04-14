""" Calcular el nuevo salario de un obrero si obtuvo un incremento de un 25 por ciento de su salario anterior. """

salario = input ('Ingrese su salario anterior: ')
aumento = (float(salario) * 0.25)
total = salario + aumento
print ('Tiene un incremento de: %2.f') % (aumento)
print ('Su nuevo salario es: %2.f') % (total)
