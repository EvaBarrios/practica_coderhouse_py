edad = int(input("Ingrese edad: "))
antiguedad = int(input("Ingrese antigueadad en su trabajo en anios: "))
ingreso = int(input("Ingreso mensual: "))

if edad >=18:
    if antiguedad >= 3:
        if ingreso> 2500:
            print("Credito aprobado")
        else:
            print("Credito no aprobado")
    else:
        if ingreso >= 4000:
            print("Credito aprobado")
        else:
            print("Credito no aprobado")
else:
    print("No se aprueba el credito por ser menor de edad")
    

    