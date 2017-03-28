import math

a = float(input("ingrese un cateto\n"))
b = float(input("ingrese el otro cateto\n"))

def hipotenusa (x, y):
	Hp = math.sqrt(( x*x + y*y))
	print("La hipotenusa de triangulo rectangulo es :")
	print(Hp)
	
hipotenusa(a, b)

input()

