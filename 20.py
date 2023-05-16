''' Escreva um programa que use uma pilha para converter um número binário para hexadecimal.
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
        base = base * 2

    return decimal


def decimal_hexadecimal(n):
    p = Pilha()

    if n == 0:
        p.inserir(0)

    while n > 0:
        r = n % 16
        n = n // 16
        if r < 10:
            p.inserir(str(r))
        else:
            p.inserir(chr(r + 55))

    hexadecimal = ''
    while not p.is_empty():
        hexadecimal += str(p.remover())

    return hexadecimal


n = input('Digite um número binário: ')
num_decimal = binario_decimal(n)
num_hexadecimal = decimal_hexadecimal(num_decimal)
print('Resultado: ', num_hexadecimal)