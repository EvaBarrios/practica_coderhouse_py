numero_1 = float(input('Ingrese primer numero: '))
numero_2= float(input('Ingrese segundo numero: '))
opcion = int(input('Ingrese alguna de las siguientes opciones 1, 2, 3, 4: '))

while opcion:
    if opcion not in range(1,4):
        print('Esta no es una opcion correcta')
    else:
        if opcion == 1: 
            print(f'La suma de los numeros ingresados es: {round(numero_1 + numero_2,2)}')
        elif opcion == 2:
            print(f'La resta del primero y el segundo es: {round(numero_1 - numero_2,2)}')
        elif opcion == 3:
            print(f'El producto del primero y el segundo es: {round(numero_1 * numero_2,2)}')
    opcion = int(input('Ingrese alguna de las siguientes opciones 1, 2, 3, 4: '))
    if opcion == 4:
        print('Fin del programa')
        break
    