#Comparación de tres numeros

num1=int(input("Ingrese el nuemro 1..."))
num2=int(input("Ingrese el numero 2..."))
num3=int(input("Ingrese el numero 3..."))

if num1>num2 or num1>num3:
    print("El numero", num1, "es el mayor")
elif num2>num1 or num2>num3:
    print("El numero", num2, "es el mayor")
elif num3>num1 or num3>num2:
     print("El numero", num3, "es el mayor")

if num1<num2 or num1<num3:
    print("El numero", num1, "es el menor")
elif num2<num1 or num2<num3:
    print("El numero", num2, "en el menor")
elif num3<num1 or num3<num2:
     print("El numero", num3, "es el menor")
