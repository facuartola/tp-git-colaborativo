# Ejercicio 1 - Caja del Kiosco

while True:
    nombre = input("Nombre del cliente: ")
    if nombre.isalpha():
        break
    print("Error: solo letras.")

while True:
    cantidad = input("Cantidad de productos: ")
    if cantidad.isdigit() and int(cantidad) > 0:
        cantidad = int(cantidad)
        break
    print("Error: número válido mayor a 0.")

total_sin = 0
total_con = 0

for i in range(cantidad):
    while True:
        precio = input(f"Producto {i+1} - Precio: ")
        if precio.isdigit():
            precio = int(precio)
            break
        print("Error: número válido.")

    while True:
        desc = input("¿Descuento S/N?: ").lower()
        if desc in ["s","n"]:
            break
        print("Error.")

    total_sin += precio
    if desc == "s":
        total_con += precio * 0.9
    else:
        total_con += precio

print("Total sin descuentos:", total_sin)
print("Total con descuentos:", round(total_con,2))
print("Ahorro:", round(total_sin-total_con,2))
print("Promedio:", round(total_con/cantidad,2))
