print ("Ejercicio 10: Crear un programa que por medio de recursion \n calcule la suma de los cuadrados de\n numeros")
num = input("Ingrese cantidad de numeros a sumar: ")
def suma(n):
    
    if (n == 1):
        return 1
    else:
        res = (n**2) + suma(n-1)
        return res  

print(suma(num))

input()

  