""" Situacion 8 - Modulo 1"""

exaMath = float (input ('Ingrese la nota del examen de Matematicas: '))
t1math = float (input ('Nota de la tarea 1: '))
t2math = float (input ('Nota de la tarea 2:  '))
t3math = float (input ('Nota de la tarea 3: '))
pjeExaMath = exaMath * 0.90
pjeTarMath = ((t1math + t2math + t3math) / 3) * 0.10
promMath = pjeExaMath + pjeTarMath
print ('El promedio de Matematicas es: %2.f') % (promMath)

exaFis = float (input ('Nota del examen de Fisica: '))
t1fis = float (input ('Nota de la tarea 1: '))
t2fis = float (input ('Nota de la tarea 2: '))
pjeTarFis = ((t1fis + t2fis ) / 2) * 0.20
pjeExaFis = exaFis * 0.90
promFis = pjeExaFis + pjeTarFis
print ('El promedio de Fisica es: %2.f') % (promFis)

exaQui = float (input ('Ingrese la nota del examen de Quimica: '))
t1qui = float (input ('Nota de la tarea 1: '))
t2qui = float (input ('Nota de la tarea 2: '))
t3qui = float (input ('Nota de la tarea 3: '))
pjeExaQui =exaQui * 0.85
pjeTarQui = ((t1qui + t2qui + t3qui) / 3) * 0.15
promQui = pjeTarQui + pjeExaQui
print ('El promedio de Quimica es: %2.f') % (promQui)

promGral = (promMath + promFis + promQui) / 3
print ('El promedio general de las materias es: %2.f') % (promGral)
