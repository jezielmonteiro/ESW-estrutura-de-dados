# Implemente cada exercício utilizando tanto o for quanto o while.

# Ler 5 notas e informar a média.

#for
for x in range(1, 6):
    nota = float(input("Informe uma nota: "))
    soma += nota
    media = soma / 5

print(media)

#while
nota = 0
soma = 0
numero = 0

while numero <= 5:
    nota = float(input("Informe uma nota: "))
    soma += nota
    numero += 1

print(f"A média é {soma}")


# Imprimir a tabuada do número 3 (3 x 1 = 3 até 3 x 10 = 30).

#for
for x in range(1, 11):
    print("3 x {} = {}".format(x, 3 * x))

#while
numero = 1
while numero <= 10:
    print("3 x {} = {}".format(numero, 3 * numero ))
    numero += 1