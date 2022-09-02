# Este programa calcula el promedio final de un equipo de fútbol en un torneo de 20 partidos
partidos_ganados = float(input("Ingrese la cantidad de partidos ganados: "))
partidos_empatados = float(input("Ingrese la cantidad de partidos empatados: "))
partidos_perdidos = float(input("Ingrese la cantidad de partidos perdidos: "))
total_partidos_jugados = partidos_ganados+partidos_empatados+partidos_perdidos
promedio_final = (2*partidos_ganados + 1*partidos_empatados)/total_partidos_jugados
print("El promedio final es: " + str(promedio_final)) 