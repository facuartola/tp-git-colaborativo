hemisferio = input("Ingrese hemisferio (N/S): ").upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día: "))

# Determinar estación en hemisferio norte
if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
else:
    estacion_norte = "Otoño"

# Ajustar según hemisferio
if hemisferio == "N":
    print(estacion_norte)
else:
    if estacion_norte == "Invierno":
        print("Verano")
    elif estacion_norte == "Primavera":
        print("Otoño")
    elif estacion_norte == "Verano":
        print("Invierno")
    else:
        print("Primavera")
