num =[]
num = input("Llene el arreglos")
x = input("Ingrese el numero de rotacion que debe hacer")

def rotar (lista, x):
    guardar = list(lista)
    for i in range(len(lista)):

        if x<0:
            lista[i+x] = guardar[i]
        else:
            lista[i] = guardar[i-x]
        
rotar(num, -x)

print (num)
input()