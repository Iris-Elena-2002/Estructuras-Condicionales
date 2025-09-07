#Entrada del parque

edad=int(input("Ingrese la edad del visitante..."))

if edad<=12:
    print("El precio del boleto es de $50")
elif 12>edad<17:
    print("El precio del boleto es de $80")
else:
    if edad>18:
        print("El precio del boleto es de $120")