texto="Soy Laura Calle de segundo smr"
def vocales_consonante(texto):
    vocales="aeiouAEIOU"
    cuenta={"vocales":0, "consonantes":0}
    for caracteres in texto:
        if caracteres in vocales:
            cuenta["vocales"]+=1
        else:
            cuenta["consonantes"]+=1
    return cuenta

resultado=vocales_consonante(texto)
print(resultado)