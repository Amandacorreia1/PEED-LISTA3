'''Escreva um programa que use uma pilha para converter um número binário para octal.
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



def binario_decimal(n):
    p = Pilha()

    for i in n:
        p.inserir(int(i))

    decimal = 0
    base = 1
    while not p.is_empty():
        decimal = decimal + p.remover() * base
        base = base *2
      
    return decimal


def decimal_octal(n):
    p = Pilha()

    if n == 0:
        p.inserir(0)

    while n > 0:
        r = n % 8
        n = n // 8
        p.inserir(str(r))

    octal = ''
    while not p.is_empty():
        octal += str(p.remover())

    return octal


n = input('Digite um número binário: ')
num_decimal = binario_decimal(n)
num_octal = decimal_octal(num_decimal)
print('Resultado: ', num_octal)