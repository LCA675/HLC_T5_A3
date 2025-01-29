def eliminar_duplicados (texto_lista):
    texto_sin_duplicados=list(set(texto_lista))
    print("El texto sin duplicados es: ", texto_sin_duplicados)

texto=["perro", "gato", "tortuga", "gato", "canario", "elefante", "elefante"]

eliminar_duplicados(texto)