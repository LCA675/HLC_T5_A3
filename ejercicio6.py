lista_palabras=["elefante", "gato", "perro", "loro", "canario"]
def diccionario_palabras (lista_palabras):
    diccionario={palabra: len(palabra) for palabra in lista_palabras}
    return diccionario
    
resultado=diccionario_palabras(lista_palabras)
print(resultado)