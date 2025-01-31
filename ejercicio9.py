alumnos = {"Laura": 8, "Alejandro": 10, "Cristóbal": 7, "Triana": 6}

def notas_promedio(alumnos):
    nota_max = 0
    alumno_max = ""
    promedio = 0
    for nombre, nota in alumnos.items():
        if nota > nota_max:
            nota_max = nota
            alumno_max = nombre
        promedio += nota / len(alumnos)
        
    return f"Promedio: {promedio:.2f}, Nota máxima: {nota_max}, Mejor estudiante: {alumno_max}"

resultado = notas_promedio(alumnos)
print(resultado)
