 
''' Escreva um programa que leia uma expressão matemática na forma de string e 
utilize uma pilha para verificar se os parênteses estão balanceados.
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



def estaBalanceada(exp):
    p = Pilha()
    
    for caractere in exp:
        if caractere == "(":
            p.push(caractere)
        elif caractere == ")":
            if p.is_empty():
                return False
            p.pop()
    return p.is_empty()

exp = input("Digite a expressao que voce deseja: ")

if estaBalanceada(exp):
    print("parenteses balanceados") 
    
else:
    print("Parenteses não estão desbalanceados")


            
        
            


