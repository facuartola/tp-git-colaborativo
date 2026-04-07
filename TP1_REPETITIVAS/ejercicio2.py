# Ejercicio 2 - Login

usuario_ok = "alumno"
clave_ok = "python123"

intentos = 0
while intentos < 3:
    user = input("Usuario: ")
    clave = input("Clave: ")
    if user == usuario_ok and clave == clave_ok:
        print("Acceso concedido")
        break
    else:
        print("Error")
        intentos += 1

if intentos == 3:
    print("Cuenta bloqueada")
else:
    while True:
        op = input("1) Estado 2) Cambiar clave 3) Mensaje 4) Salir: ")
        if not op.isdigit():
            print("Error")
            continue
        op = int(op)
        if op == 1:
            print("Inscripto")
        elif op == 2:
            nueva = input("Nueva clave: ")
            if len(nueva) < 6:
                print("Error")
            else:
                print("Clave cambiada")
        elif op == 3:
            print("Seguí aprendiendo!")
        elif op == 4:
            break
        else:
            print("Error")
