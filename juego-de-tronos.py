import random 


def Atacar (x,y):
	if cpu == "D" and user  == "C": 
		print "Gano CPU"
		result = 1
	elif cpu == "C" and user == "D":	
		print "Gano USER"
		result = 2
	elif cpu == user:
		print "Empate"	
		result = 3
	else: 
		print ("Las acciones ingresadas no son validas")
	return result

def Contragolpear(x,y):
	if cpu == "A" and user  == "D": 
		print "Gano CPU"
		result = 1
	elif cpu == "D" and user == "A":	
		print "Gano USER"
		result = 2
	elif cpu == user:
		print "Empate"	
		result = 3
	else: 
		print ("Las acciones ingresadas no son validas")
	return result

def Defender_Con_Escudo(X,Y):
	if cpu == "C" and user  == "A": 
		print "Gano CPU"
		result = 1
	elif cpu == "A" and user == "C":	
		print "Gano USER"
		result = 2
	elif cpu == user:
		print "Empate"	
		result = 3
	else: 
		print ("Las acciones ingresadas no son validas")
	return result


cond = raw_input ("Para comenzar la partida presione S, Para salir cualquier tecla:  ").upper()
puntcpu = 0
puntuser = 0
flags = True
while cond == "S" or flags == False:
	if flags:
			ronda = 5
	else:
			ronda = 1
	while ronda > 0 :
		print ""
		print "Ingrese el movimiento que desea hacer: "
		mov = raw_input ("Atacar A, Defender con escudo D, Contragolpear C :  ").upper()
		if mov == "A":
			cpu = random.choice(['C', 'D',])
			print "Ingrese la accion que desea hacer:"
			user= raw_input ("Defender con escudo D, Contragolpear C ").upper()
			print ""
			if user == "C" or user == "D":
				combate = Atacar(cpu,user)
				if combate == 1:
					puntcpu = puntcpu + 5
				elif combate == 2:
					puntuser = puntuser + 5
				else:
					puntcpu = puntcpu + 1
					puntuser = puntuser + 1
			else:
				print "Ingreaste mal la accion, PRESTA ATENCION e intentalo de nuevo"
				ronda = ronda + 1
		elif mov == "C":
			cpu = random.choice(['A', 'D',])
			print "Ingrese la accion que desea hacer:"
			user= raw_input ("Atacar A, Defender con escudo D ").upper()
			print ""
			if user == "A" or user == "D":
				combate = Contragolpear(cpu,user)	
				if combate == 1:
					puntcpu = puntcpu + 5
				elif combate == 2:
					puntuser = puntuser + 5
				else:
					puntcpu = puntcpu + 1
					puntuser = puntuser + 1		
			else:
				print "Ingreaste mal la accion, PRESTA ATENCION e intentalo de nuevo"
				ronda = ronda + 1
		elif mov == "D":
			cpu = random.choice(['A', 'C',])
			print "Ingrese la accion que desea hacer:"
			user= raw_input ("Atacar A, Contragolpear C ").upper()
			print ""
			if user == "A" or user == "C":
				combate = Defender_Con_Escudo(cpu,user)	
				if combate == 1:
					puntcpu = puntcpu + 5
				elif combate == 2:
					puntuser = puntuser + 5
				else:
					puntcpu = puntcpu + 1
					puntuser = puntuser + 1		
			else:
				print "Ingreaste mal la accion, PRESTA ATENCION e intentalo de nuevo"
				ronda = ronda + 1
		else:
			print ""
			print "Ingreaste mal el movimiento, PRESTA ATENCION e intentalo de nuevo"
			ronda = ronda + 1
		ronda = ronda - 1
	print ""
	print "Tus puntos son: ",puntuser
	print "Los puntos de la cpu son: ",puntcpu
	print ""
	if puntuser == puntcpu:
		print "PARTIDA EMPATADA"
		print "RONDA DE DESEMPATE"
		flags = False
	elif puntuser > puntcpu:
		print "Ganaste la partida"
		print ""
		cond = raw_input ("Si deseas seguir jugando presiona S, para salir cualquier tecla ").upper()
		flags = True
		puntcpu = 0
		puntuser = 0
	else:
		print "Perdiste la partida"
		print "Intentalo de nuevo"
		print ""
		cond = raw_input ("Si deseas seguir jugando presiona S, para salir cualquier tecla ").upper()
		flags = True
		puntcpu = 0
		puntuser = 0
print ""
print "Juego creado Tato Developer JR en Qbits"
print "Seguinos en nuestra fanpage: www.facebook.com/qbits.ar"
print "INFORMATORIO 2016"