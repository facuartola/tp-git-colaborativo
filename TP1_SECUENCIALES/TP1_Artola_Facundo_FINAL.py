# Trabajo Práctico 1 - Estructuras Secuenciales
# Alumno: Artola Facundo

# Nota: cada ejercicio se puede ejecutar desde el menú.
# Traté de hacerlo simple y claro para que se entienda bien cada paso.

def suma_dos_numeros():
    num1 = float(input("Ingresá el primer número: "))
    num2 = float(input("Ingresá el segundo número: "))

    resultado = num1 + num2
    print("El resultado de la suma es:", resultado)


def doble_numero():
    numero = float(input("Ingresá un número: "))

    doble = numero * 2
    print("El doble es:", doble)


def area_rectangulo():
    base = float(input("Ingresá la base: "))
    altura = float(input("Ingresá la altura: "))

    area = base * altura
    print("El área del rectángulo es:", area)


def celsius_a_fahrenheit():
    celsius = float(input("Ingresá la temperatura en °C: "))

    fahrenheit = (celsius * 9/5) + 32
    print("Temperatura en Fahrenheit:", round(fahrenheit, 2))


def promedio():
    n1 = float(input("Ingresá el primer número: "))
    n2 = float(input("Ingresá el segundo número: "))

    prom = (n1 + n2) / 2
    print("El promedio es:", round(prom, 2))


def menu():
    opcion = -1

    while opcion != 0:
        print("\n========= MENÚ =========")
        print("1 - Sumar dos números")
        print("2 - Calcular doble")
        print("3 - Área de rectángulo")
        print("4 - Convertir °C a °F")
        print("5 - Promedio de dos números")
        print("0 - Salir")

        opcion = int(input("Elegí una opción: "))

        if opcion == 1:
            suma_dos_numeros()
        elif opcion == 2:
            doble_numero()
        elif opcion == 3:
            area_rectangulo()
        elif opcion == 4:
            celsius_a_fahrenheit()
        elif opcion == 5:
            promedio()
        elif opcion == 0:
            print("Programa finalizado.")
        else:
            print("Opción inválida, intentá de nuevo.")


# Punto de entrada del programa
menu()
