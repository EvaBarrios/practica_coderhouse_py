nombre = input("Como te llamas? ")
preferencia = input("Ingresa preferencia: \n M: Marvel \n C: Capcom \n ")

nombre = nombre.capitalize()
preferencia = preferencia.capitalize()

if "A"<=nombre[0]<="M" and preferencia=="M" or nombre[0]>"M" and preferencia=="C":
    print("Perteneces al grupo A")
else:
    print("Perteneces al grupo B")