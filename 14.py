''' Escreva um programa que leia uma expressão matemática na forma de string e 
utilize uma pilha para converter a expressão para a notação polonesa reversa.
'''
class Item: 
    def __init__(self, valor):
        self.valor = valor
        self.next = None

class Pilha:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, valor): 
        novoItem = Item(valor)
        novoItem.next = self.top
        self.top = novoItem
        self.size += 1
        
    def pop(self): 
        if self.size == 0:
            raise Exception("A pilha está vazia!")
        valor = self.top.valor
        self.top = self.top.next
        self.size -= 1
        return valor
    
    def topo(self):
        if self.size == 0:
            raise Exception ("A pilha está vazia!")
        return self.top.valor

    def is_empty(self):
        return self.size == 0
    
    def _len_(self):
        return self.size
    
def verificar(exp):
    pilha = Pilha()
    for p in exp:
        if p == '(':
            pilha.push(p)
        elif p == ')':
            if len(pilha) > 0:
                pilha.pop()
            else:
                pilha.push(p)
    return pilha.is_empty()

def infixaParaPosfixa(expressao):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    operadores = Pilha()
    posfixa = []
    numeros = '0123456789'
    for caracter in expressao:
        if caracter in numeros:
            posfixa.append(caracter)
        elif caracter == '(':
            operadores.push(caracter)
        elif caracter == ')':
            while operadores.topo() != '(':
                posfixa.append(operadores.pop())
            operadores.pop()
        elif caracter in precedencia:
            while not operadores.is_empty()  \
                and operadores.topo() != '(' \
                and precedencia[caracter] <= precedencia[operadores.topo()]:
                posfixa.append(operadores.pop())
            operadores.push(caracter)
    while not operadores.is_empty():
        posfixa.append(operadores.pop())
    return ''.join(posfixa)

expres = input('Digite a expressão: ')
resposta = infixaParaPosfixa(expres)
print('Reesultado: ', resposta)