'''Escreva um programa que leia uma expressão matemática na forma de string e 
utilize uma pilha para calcular o resultado da expressão na notação polonesa reversa.'''


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

def infixa_para_posfixa(expressao):
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


def calcular(exp):
    p = Pilha()
    
    for caractere in exp:
        if caractere.isdigit():
            p.push(caractere)
        else:
            n1 = p.pop()
            n2 = p.pop()
            if caractere == "+":
                r = int(n1) + int(n2)
                p.push(str(r))

            if caractere == "-":
                r = int(n1) - int(n2)
                p.push(str(r))
    
                
            if caractere == "*":
                r = int(n1) * int(n2)
                p.push(str(r))

            if caractere == "/":
                r = int(n1) / int(n2)
                p.push(str(r))

    return p.pop()


s = input("Digite a expressão: ")
pos = infixa_para_posfixa(s)
r = calcular(pos)
print("Resultado", r)

    
                
                
                
                
                