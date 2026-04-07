consumo = float(input("Ingrese el consumo en kWh: "))

if consumo < 150:
    print("Consumo bajo")
elif consumo <= 300:
    print("Consumo medio")
else:
    print("Consumo alto")

if consumo > 500:
    print("Considere medidas de ahorro energético")
