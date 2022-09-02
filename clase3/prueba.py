print("a">"b") #Cuando comparamos cadenas, comparamos sus valores Unicode.
#POR ESO ESTO IMPRIME FALSE
# El valor booleano de cualquier string distinto de vacio es True

print("True" and "False") # Como bool("True")=True, evalua bool("False")=True e imprime "False"
print("False" and "True") # Como bool("False")=True, evalua bool("Tue")=True e imprime "True"
print(True and False) # es False
print(False and True) # es False
print(True and False=="True" and "False") # es False: el primero es bool y el segundo es str?

print(bool("True"))
print(bool("False"))

print(type("True" and "False"))
print(type("False" and "True"))
print(type(True and False))
print("True" and "hola") # imprime "hola"
print("hola" and "True") # imprime "True"
print("False" and "hola") # imprime "hola"
print("hola" and "False") #imprime "False"
print("A" and "B") # imprime "B"
print("A" or "B") # imprime "A"
print("" and "a") # no imprime nada ya que bool("" and "a") es False
print("a" and "")  # no imprime nada ya que bool("" and "a") es False
print("" and not"")  # no imprime nada ya que bool("" and not"") es False
print("a" and not"") # evalua bool("a")= True y pasa a evaluar bool(not "")=True e imprime "True"
print(not"" and "a") # evalua bool(not "")=True y pasa a evaluar bool("a")=True e imprime "a"