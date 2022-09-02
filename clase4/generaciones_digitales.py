agno = int(input("Ingrese año de nacimiento: "))

if 1920<=agno<=1940:
    print("Perteneces a la GENERACION SILENCIOSA")
elif 1946<=agno<=1964:
    print("Perteneces a la GENERACION BABY BOOMER")
elif  1965<=agno<=1979:
  print("Perteneces a la GENERACION X")  
elif 1980<=agno<=2000:
    print("Perteneces a la GENERACION Y")
elif 2001<=agno<=2010:
    print("Perteneces a la GENERACION Z")
else:
    print("No existe generacion asociada")
