#Situacion 1:
#Calcular que edad tendra una persona en un anio futuro,
#teniendo en cuenta el anio de su nacimiento

nac = input ('Ingrese su fecha de nacimiento: ')
futuro = input ('Que edad tendra en el anio?: ')
final = futuro - nac
print ('En el anio %d tendra %d anios.') % (futuro, final)
