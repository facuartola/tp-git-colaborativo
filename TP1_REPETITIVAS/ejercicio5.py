# Ejercicio 5 - Gladiador

while True:
    nombre = input("Nombre: ")
    if nombre.isalpha():
        break

vida = 100
enemigo = 100

while vida > 0 and enemigo > 0:
    op = input("1 Atacar 2 Curar: ")
    if op == "1":
        enemigo -= 15
    elif op == "2":
        vida += 10

    enemigo -= 12

if vida > 0:
    print("Victoria")
else:
    print("Derrota")
