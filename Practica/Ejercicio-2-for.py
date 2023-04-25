vocales = ("a", "e", "i", "o", "u")
contVocal = 0
contCons = 0
for i in range(10):
    letra = input("Ingrese una letra: ").lower()
    if letra in vocales:
        contVocal += 1
    else:
        contCons += 1

print(f"\nVocales = {contVocal}\nConsonantes = {contCons}")


    