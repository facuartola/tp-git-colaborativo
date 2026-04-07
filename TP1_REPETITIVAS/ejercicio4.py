# Ejercicio 4 - Escape Room (simplificado)

energia = 100
tiempo = 12
cerraduras = 0

while energia > 0 and tiempo > 0 and cerraduras < 3:
    print("Energia:", energia, "Tiempo:", tiempo)
    op = input("1 Forzar 2 Salir: ")
    if op == "1":
        energia -= 20
        tiempo -= 2
        cerraduras += 1
    else:
        break

if cerraduras == 3:
    print("Victoria")
else:
    print("Fin del juego")
