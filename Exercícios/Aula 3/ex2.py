# Lista: Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros e os armazene dentro de uma lista. Após a leitura, 
# crie outra estrutura de repetição para somar todos os valores digitados.

lista = []
for x in range(1, 6):
    num = int(input("Digite um número: "))
    lista.append(num)

soma = 0
for y in range(
    len(lista)
):
    soma += lista[
        y
    ]

print(f"Soma: {soma}")