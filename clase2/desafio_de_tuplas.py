tupla = (8, 15, 4, 39, 5, 89, 19, 7, -755, 88, 123, 2, 11, 15, 9, 355)
print("El último elemento de la tupla es " + str(tupla[-1]))
print("El número de ítems de la tupla es " + str(len(tupla)))
# print("La posición del ítem 87 de la tupla es "+ str(tupla.index(87)))
Lista = list(tupla[-3:]) # Creo lista con los 3 últimos elementos de la tupla
print(Lista)
print("Posición 8 de la tupla: " + str(tupla[7]))
print("El número 7 aparece "+ str(tupla.count(7))+" vez/veces en la tupla")