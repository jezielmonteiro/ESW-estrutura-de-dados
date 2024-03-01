"""Leia a idade do usuário e classifique-o em:"""
""" - Criança - 0 a 12 anos"""
""" - Adolescente - 13 a 17 anos"""
""" - Adulto - acima de 18 anos"""
""" - Se o usuário digitar um número negativo, mostrar a mensagem que a idade é inválida"""

idade = int(input("Informe sua idade: "))
if (idade > 0):
    print(f"Idade: {idade} anos")
if (0 < idade < 12):
    print("Você é uma criança!")
if (13 < idade < 17):
    print("Você é um adolescente!")
if (idade >= 18):
    print("Você é um adulto!")
if (idade < 0):
    print("Idade inválida.")