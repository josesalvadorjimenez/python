import math
radio = input("Ingrese el radio la medida del radio: ")

def volumeEsfera(R):
	volumen = (4 * math.pi * radio**3)
	print("El volumen de la esfera es :", volumen)
	return
volumeEsfera(radio)
input()
