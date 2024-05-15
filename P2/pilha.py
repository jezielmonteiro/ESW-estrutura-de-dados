import numpy as np

class Pilha:
    def __init__(self, capacidade):
        self.__capacidade = capacidade #Define a capacidade da pilha
        self.__topo = -1  #Valor do topo da pilha
        self.__valores = np.empty(self.__capacidade, dtype=int)  #Array de valores

    def __pilha_cheia(self): #Retorna "True" se a pilha estiver cheia
        return self.__topo == self.__capacidade - 1 

    def __pilha_vazia(self): #Retorna "True" se a pilha estiver vazia
        return self.__topo == -1 

    def empilhar(self, valor): #Insere um valor ao topo da pilha
        if self.__pilha_cheia():
            print("A pilha está cheia")
        else:
            self.__topo += 1
            self.__valores[self.__topo] = valor

    def desempilhar(self): #Desempilha um item da pilha e retorna o valor que agora está no topo da pilha
        if self.__pilha_vazia():
            print("A pilha está vazia")
            return -1
        else:
            valor = self.__valores[self.__topo]
            self.__topo -= 1
            return valor

    def verTopo(self): #Retorna o valor do topo da pilha
        if self.__topo != -1:
            return self.__valores[self.__topo]
        else:
            return -1

pilha = Pilha(6)

print(pilha.verTopo())
pilha.empilhar(1)
print(pilha.verTopo())
pilha.desempilhar()
pilha.empilhar(5)
pilha.empilhar(6)
pilha.empilhar(7)
pilha.empilhar(3)
pilha.empilhar(4)
pilha.empilhar(2)
pilha.empilhar(8)
print(pilha.verTopo())
pilha.desempilhar()
print(pilha.verTopo())




