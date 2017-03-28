num1 = float(input("Ingrese el primero numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))


def maxi(x,y,z):
	if(x > y and x > z):
		print ("El mayor es: ",(x))
	elif(y > x and y > z):
		print ("El numero es: ", (y))
	else:
		print ("El mayor es:", (z))
	return
maxi(num1,num2,num3)

input()