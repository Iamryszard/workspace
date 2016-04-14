""" Realice el programa que permita ingresar un precio y devuelva como resultado el precio con el IVA incluido (+21%) """

precio = input ('Ingrese un precio: ')
con_iva = (float(precio) * 0.21)
total = precio + con_iva
print ('El resultado del precio con IVA es: %.2f') % (total)
