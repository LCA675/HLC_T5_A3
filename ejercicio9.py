alumnos=["Laura":8, "Alejandro":10, "Cristóbal":7, "Triana":8]
def notas_promedio(alumnos):
    promedio=alumnos.values/len(alumnos)
    mejor_alumno=max(alumnos, valor=alumnos.get)
    return promedio
    return mejor_alumno

promedio, mejor_alumno=notas_promedio(alumnos)
print(f"El mejor alumno es:", mejor_alumno)
print(f"El promedio es: ", promedio)
