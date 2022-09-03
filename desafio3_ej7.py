lista_1 = ['h','o','l','a',' ', 'm','u','n','d','o']
lista_2 = ['h','o','l','a',' ', 'l','u','n','a']
lista_3 = []

for i in range(len(lista_1)):
    if lista_1[i] in lista_2 and lista_1[i] not in lista_3:
        lista_3.append(lista_1[i])

print(f'La lista_1 es: {lista_1}')
print(f'La lista_2 es: {lista_2}')
print(f'La siguiente lista contiene (sin repetir) los elementos "repetidos" en lista_1 y lista_2: {lista_3}')