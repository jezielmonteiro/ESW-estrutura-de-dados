# Leia a idade do usuário e classifique-o em:
# - Criança - 0 a 12 anos
# - Adolescente - 13 a 17 anos
# - Adulto - acima de 18 anos
# - Se o usuário digitar um número negativo, mostrar a mensagem que a idade é inválida

while True:
    idade = int(input("\nInforme sua idade: "))
    if (idade > 0):
        print(f"\nIdade: {idade} anos")
    if (0 < idade <= 12):
        print("\nVocê é uma criança!\n")
        break
    if (13 < idade <= 17):
        print("\nVocê é um adolescente!\n")
        break
    if (idade >= 18):
        print("\nVocê é um adulto!\n")
        break
    if (idade < 0):
        print("\nIdade inválida.")