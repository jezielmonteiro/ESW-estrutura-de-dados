# Dicionário: Crie um dicionário para armazenar o nome e a idade de 3 piratas, fazendo a leitura dos valores por 
# meio de uma estrutura de repetição. Depois, crie uma nova estrutura de repetição para somar todas as idades e 
# retornar a média.

piratas = {}
for p in range(1, 4):
    name = input("Informe o nome do pirata: ")
    idade = int(input("Informe a idade do pirata: "))
    piratas[name] = idade 

soma = 0
for idade in piratas.values():
    soma += idade

print(f"Média: {round(soma / 3, 1)}")