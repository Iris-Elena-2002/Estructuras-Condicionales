#AÑO BISIESTO

año=int(input("Ingrese un año"))

if año%4==0:
   print("El año es bisiesto")
elif año%400==0:
   print("El año es bisiesto")
else:
   if año%100==0:
    print ("El año no es bisiesto")