""" Situacion 9 """

print 'Ingrese opcion! '
print '1 - Calcular el area de un triangulo.'
print '2 - Calcular el area de un circulo.'
opcion = int (input ("Que desea hacer?: "))
if (opcion == 1):
    area = float (input ('Ingrese la base: '))
    altura = float (input ('Ingrese la altura: '))
    areaT = (base * altura) / 2
    print ('El area del triangulo es: %2.f' % (areaT))
else:
    radio = float (input ('Ingrese el radio: '))
    areaC = 3.14 * (radio ** 2)
    print ('El area del circulo es: %2.f' % (areaC))
