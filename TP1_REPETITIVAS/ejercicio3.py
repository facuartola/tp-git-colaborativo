# Ejercicio 3 - Agenda simple

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

while True:
    op = input("1 Reservar 2 Salir: ")
    if op == "1":
        nombre = input("Nombre: ")
        if nombre.isalpha():
            if lunes1 == "":
                lunes1 = nombre
            elif lunes2 == "":
                lunes2 = nombre
            elif lunes3 == "":
                lunes3 = nombre
            elif lunes4 == "":
                lunes4 = nombre
            else:
                print("Lleno")
    elif op == "2":
        break
