print("Ingresa 3 numeros para sacarle la media\n")

suma1 = float(input("Ingrese el primer umero: "))
suma2 = float(input("Ingrese el segundo numero: "))
suma3 = float(input("Ingresa el tercer numero: "))

def media (x, y, z):
	media=(x + y + z)/3
	print("La media de ", x," ", y, " y ", z, " es ", media)
	return
media(suma1, suma2, suma3)

input()
