""" Situacion C3 """

num1 = int (input ('Ingrese un valor: '))
num2 = int (input ('Ingrese segundo valor:'))
num3 = int (input ('Ingrese tercer valor: '))
if (num1 < num2) & (num1 < num3):
    if (num2 < num3):
        print ('Ordenados de menor a mayor: ', num1, ' ', num2, ' ', num3)
    else:
        print ('El orden ascendente es: ', num1, ' ', num3, ' ', num2)
else:
    if (num2 < num1)  & (num2 < num3):
        if (num1 < num3):
            print ('Ordenados de menor a mayor: ', num2, ' ', num1, ' ', num3)
        else:
            print ('El orden ascendente es: ', num2, ' ', num3, ' ', num1)
    elif (num3 < num1) & (num3 < num2):
        if (num1 < num2):
            print ('El orden ascendente es: ', num3, num1, num2 )
        else:
            print ('Ordenados de menor a mayor: ', num3, num2, num1)
