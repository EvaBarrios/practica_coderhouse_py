def es_entero(cadena):
    try:
        int(cadena)
        return True   
    except:
        return False
    
    
def es_palabra(cadena):
    try:
        str(cadena)
        return True
    except:
        return False
    
    
def es_real(cadena):
    try:
        float(cadena)
        return True
    except:
        return False
    
    
cadena = input("ingrese cadena: ")
if es_entero(cadena):
    print('Usted ingreso un numero entero')
elif es_real(cadena):
    print('Usted ingreso un numero real no entero')
else:
    print('Usted ingreso caracteres')
    
