""" La presion, el volumen y la temperatura de una masa de aire se relacionan por la formula de masa = (presion x volumen) / ((0,37 x (T + 460))).
El programa debe obtener los datos para calcular la masa. """

presion = input ('Ingrese la presion: ')
volumen = input ('Ingrese el volumen: ')
temp = input ('Ingrese temperatura: ')
masa = (presion * volumen) / ((0,37 * (temp + 460)))
