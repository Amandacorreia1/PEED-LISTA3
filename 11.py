''' Escreva um programa que use uma pilha para ordenar uma lista de inteiros em ordem crescente.
'''

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Pilha:
    def __init__(self):
        self._topo = None
        self.tamanho = 0
   
    def __len__(self):
        return self.tamanho
   
    def is_empty(self):
        return self.tamanho == 0
   
    def inserir(self, valor):
        no = No(valor)
        no.proximo = self._topo
        self._topo = no
        self.tamanho += 1
   
    def remover(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia")
        valor = self._topo.valor
        self._topo = self._topo.proximo
        self.tamanho -= 1
        return valor
   
    def topo(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia")
        return self._topo.valor
    

    
def ordenar_numeros():
    numeros = input("Digite os números que deseja ordenar, separados por espaços: ").split()
    pilha = Pilha()
    for numero in numeros:
        pilha.inserir(int(numero))
    
    lista_ordenada = []
    while not pilha.is_empty():
        lista_ordenada.append(pilha.remover())
    
    return lista_ordenada


lista_ordenada = sorted(ordenar_numeros())
print(lista_ordenada)
    
    
    
    
    
    
    
    
    
    
  