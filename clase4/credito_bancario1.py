edad = int(input("Ingrese edad: "))
antiguedad = int(input("Ingrese antigueadad en su trabajo en anios: "))
ingreso = int(input("Ingreso mensual: "))

if edad >=18 and antiguedad>=3 and ingreso>2500 or ingreso>=4000:
    print("Credito aprobado")
else:
    print("Credito NO aprobado")