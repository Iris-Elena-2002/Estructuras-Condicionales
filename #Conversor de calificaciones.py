#Conversor de calificaciones

cal=int(input("Ingrese una calificacion (0-100)..."))

if 90<=cal<=100:
    print("La calificación es una A")
elif 80<= cal<=89:
    print("La calificación es una B")
elif 70<=cal<=79:
    print("La calificación es una C")
elif 60<= cal <=69:
    print("La calificación es una D")
else:
    if cal<60:
     print("La calificación es una F")
