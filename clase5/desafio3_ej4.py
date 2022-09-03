while True:
    contador = input("Cuantos numeros ingresara por consola?: ")
    if str.isdigit(contador):
        break
    
n = int(contador)
lista = []    
for i in range(n):
    num = float(input("Ingrese numero: "))
    lista.append(num)
# print(lista)
    
print(f'La media aritmetica de los numeros ingresados es: {sum(lista)/n}')
