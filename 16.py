'''Escreva um programa que use uma pilha para converter um número hexadecimal para decimal. conferir depois.
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


def hexa_decimal(n):
    p = Pilha()

    for i in n:

        if i.isdigit():
            p.inserir(int(i))
        elif i == 'a' or i == 'A':
            p.inserir(10)
        elif i == 'b' or i == 'B':
            p.inserir(11)
        elif i == 'c' or i == 'C':
            p.inserir(12)
        elif i == 'd' or i == 'D':
            p.inserir(13)
        elif i == 'e' or i == 'E':
            p.inserir(14)
        elif i == 'f' or i == 'F':
            p.inserir(15)
        

    soma = 0
    base = 1

    while not p.is_empty():
        soma += p.remover() * base
        base *= 16

    return soma


n = input('Digite um numero: ')
r = hexa_decimal(n)
print(r)