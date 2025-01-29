numeros=[1, 6, 3, 8, 2, 23, 76, 12, 5, 1]

def imprimir_lista(numeros):
    print(numeros)

def suma(numeros):
    suma=0
    for i in range(len(numeros)):
        suma+= numeros[i]
    return suma 

suma=suma(numeros)
lista=imprimir_lista(numeros)
print(lista)
print("La suma es: ", suma)
print("El promedio es: ",suma/len(numeros))

