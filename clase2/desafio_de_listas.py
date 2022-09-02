LISTA1 = ["Eva", 41, "Santi", ["Fran", "Pablo", "Tomi"]]
LISTA2 = ["Jorge", 36, "genio"]
print(LISTA1)
print(LISTA2)
LISTA1.append(456789)
LISTA1.append("Hola Mundo")
LISTA2.append("Hola y Adios")
LISTA2.append(5555)
print(LISTA1)
print(LISTA2)
LISTA3 = LISTA1[0:-1]
LISTA4 = LISTA2[1:-1]
print(LISTA3)
print(LISTA4)
LISTA5 = LISTA4 + LISTA3
print(LISTA5)