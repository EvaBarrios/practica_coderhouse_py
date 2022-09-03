""" numero = int(input('Ingrese un numero impar: '))
while numero % 2 == 0:
    numero = int(input('El numero ingresado no es impar.\nPor favor ingrese un numero impar: '))
print(f'El numero {numero} es impar.\n "Fin del programa"') """

while True:
    numero = int(input('Por favor, ingrese numero impar: '))
    if numero % 2 != 0:
        break
print(f'El numero {numero} es impar.\n "Fin del programa"')