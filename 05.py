''' Escreva um programa que use uma pilha para verificar se uma string é um palíndromo 
(ou seja, se é igual quando lida de trás para frente).
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

def string(palavra):
    p = Pilha()
    
    for i in palavra:
        p.inserir(i)
        
    for i in palavra:
         if p.remover() != i:
            return False
    
    return True

palavra = input("Digite uma palavra: ")
if string(palavra):
    print("A palavra é um palíndromo")
else:
    print("A palavra não é um palíndromo")
        