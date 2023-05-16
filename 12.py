''' Escreva um programa que leia uma string contendo números e use uma pilha para converter
 a string em um número decimal.
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

def string_decimal(palavra):
    p = Pilha()
    
    for digito in range(len(palavra)-1, -1, -1): 
        if palavra[digito].isdigit():
            p.inserir(palavra[digito])
    
    j = ''
    while not p.is_empty():
        j += p.remover()
    return j

numero = (input('Informe a palavra com números que deseja converter para decimal: '))
decimal = string_decimal(numero)
print('Em decimal: ', decimal)
