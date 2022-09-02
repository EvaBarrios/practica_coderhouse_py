def if_integer(string):
    try:
        int(string)
        return True   
    except:
        return False
        
        
suma = 0
num = input('Ingrese numero entero para sumar, "exit" para finalizar :')
while num!='exit':
    if if_integer(num):
        suma += int(num)
    num = input('Ingrese numero entero para sumar, "exit" para finalizar :')
print(f'La suma de los numeros enteros ingresados es igual a {suma}')

    
    
    
    
    
    

