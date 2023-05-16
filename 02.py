'''Escreva um programa que leia uma string e use uma pilha para inverter a ordem das palavras.
'''
class Item:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Pilha:
    def __init__(self):
        self.top = None
        self.size = 0
        
    def push(self, value):
        novoItem = Item(value)
        novoItem.next = self.top
        self.top = novoItem
        self.size += 1
        
    def pop(self):
        if self.size == 0:
            raise Exception("A pilha está vazia")
        valor = self.top.value
        self.top = self.top.next
        self.size -= 1
        return valor

    def topo(self):
        if self.size == 0:
            raise Exception("A pilha está vazia")
        return self.top.value

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size


def ordem_palavra(frase):
    t = frase.split()
    p = Pilha()

    for palavra in t:
        p.push(palavra)

    inversa = ''

    while not p.is_empty():
        inversa += p.pop() + ' '
    return inversa


text = input("Digite a frase que voce deseja: ")
r = ordem_palavra(text)
print('A frase inversa: ', r)
