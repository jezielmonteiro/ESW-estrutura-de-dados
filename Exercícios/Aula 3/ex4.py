# Matriz: Dada a matriz abaixo, construa uma estrutura de repetição para percorrer e somar todos os elementos da 
# matriz.

import numpy as np

matriz = np.array([[3, 4, 1], [3, 1, 5]])

soma = 0

for x in range(matriz.shape[0]):
    for y in range(matriz.shape[1]):
        soma += matriz[x][y]

print(f"Soma: {soma}")
