def num_pares():
    numeros=[1, 2 , 3 ,4 ,5 ,6 ,7 ,8 ,9 ,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    for i in numeros:
        if i % 2==0:
            numeros.remove(i)
    return numeros

print("Los números son: ",num_pares())