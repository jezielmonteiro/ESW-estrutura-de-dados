import numpy as np

class FilaCircular:
    def __init__(self, capacidade):
        self.capacidade = capacidade #Define a capacidade da fila circular
        self.inicio = 0
        self.final = -1
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def enfileirar(self, valor):
        if (self.__fila_cheia()):   #Adiciona um valor ao final da fila circular
            print("A fila está cheia")
            return

        if (self.final == self.capacidade - 1):  
            self.final = -1  
        self.final += 1  
        self.valores[self.final] = valor 
        self.numero_elementos += 1 

    def desenfileirar(self):  #Remove o primeiro elemento da fila e retorna o segundo valor que agora está no início da fila
        if self.__fila_vazia():
            print("A fila já está vazia")
            return

        temp = self.valores[self.inicio] 
        self.inicio += 1 
        if (
            self.inicio == self.capacidade
        ): 
            self.inicio = 0 
        self.numero_elementos -= 1  
        return temp
    
    def __fila_vazia(self): #Retorna "True" se a fila estiver vazia
        return self.numero_elementos == 0

    def __fila_cheia(self): #Retorna "True" se a fila estiver cheia
        return (self.numero_elementos == self.capacidade)

    def primeiro(self):  #Retorna o primeiro valor da fila
        if (self.__fila_vazia()):
            return -1
        return self.valores[self.inicio]
    
fila = FilaCircular(6)

print(fila.primeiro())
fila.enfileirar(5)
fila.enfileirar(6)
fila.enfileirar(7)
fila.enfileirar(3)
print(fila.primeiro())
fila.enfileirar(4)
fila.enfileirar(2)
fila.enfileirar(8)
print(fila.primeiro())
fila.desenfileirar()
print(fila.primeiro())
fila.desenfileirar()
print(fila.primeiro())

