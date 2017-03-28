print("Ejercicio 8. Realiza un programa que permita generar un intervalo de n numeros entre 20 y 60")


n = int(input("Igrese la cantida de intervalo  a imprimir entre el arreglo 20 a 60 "))
def intervalo(b):

	a = range(20, 60)
	for i in range(len(a)):
		if b < len(a):
			if i <= b:
				print (i, " ", a[i])
		else:
			print ("Esta fuera de rango ")
intervalo(n)
input()