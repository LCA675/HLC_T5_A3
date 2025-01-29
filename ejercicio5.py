def texto_cuenta():
    texto="Hoy hace un día soleado, aunque hoy empezó el día nublado, hace buen tiempo"
    palabras=texto.split()
    cuenta={}
    for palabras in palabras:
        if palabras in cuenta:
            cuenta[palabras]+=1
        else:
            cuenta[palabras]=1
    return cuenta
    
resultado=texto_cuenta()
print("Se han repetido las siguientes palabras: ",resultado)