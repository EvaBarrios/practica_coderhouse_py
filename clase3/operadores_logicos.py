expresiones = [not False, not 3==5, 33/3==11 and 5>2, True or False, True*5==2.5*2 or 123>=23, 12>7 and True<False]
valores_logicos=[True, True, True, True, True, False] # "adivino" el valor lógico de los elementos de la lista
valores_logicos_reales=[bool(expresiones[0]), bool(expresiones[1]), bool(expresiones[2]), bool(expresiones[3]),bool(expresiones[4]), bool(expresiones[5])]
# acá hallé el valor lógico de cada elemento de la lista con la función bool
print(valores_logicos==valores_logicos_reales)