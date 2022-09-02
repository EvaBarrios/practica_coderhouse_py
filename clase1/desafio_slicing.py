cadena = "acitametaM ,5.8 ,otipeP ordeP"
cadena_volteada = cadena[::-1]
# print(cadena_volteada)
nombre_alumno = cadena_volteada[:12]
nota = cadena_volteada[14:17]
materia = cadena_volteada[19:29]
cadena_formateada = nombre_alumno +" ha sacado un "+ nota + " en " + materia
print(cadena_formateada)
