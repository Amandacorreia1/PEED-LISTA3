''' Escreva um programa que use uma pilha para converter um número octal para decimal.
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


def octal_decimal(n):
    p = Pilha()

    for i in n:
        p.inserir(int(i))

    soma = 0
    base = 1

    while not p.is_empty():
        soma += p.remover() * base
        base *= 8

    return soma


n = input('Digite um numero: ')
r = octal_decimal(n)
print(r)