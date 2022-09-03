valor = int(input('Ingrese un numero entero que sea mayor o igual a 0 y menor o igual a 9: '))
while valor not in range(0,10):
    valor = int(input('Por favor, ingrese numero que sea mayor o igual a 0 y menor o igual a 9: '))

lista = [1, 3, 6, 9]
if valor in lista:
    print(f'El numero {valor} se encuentra en la lista {lista}')
else:
    print(f'El numero {valor} no se encuentra en la lista {lista}')
