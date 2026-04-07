texto = input("Ingrese una palabra o frase: ")

if texto[-1].lower() in "aeiou":
    print(texto + "!")
else:
    print(texto)
