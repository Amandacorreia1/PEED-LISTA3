'''Escreva um programa que leia uma string contendo caracteres (, ), {, }, [ e ],
 e use uma pilha para verificar se os caracteres estão balanceados
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
    
def estaBalanceado(expressao):
    pilha = Pilha()
    abertura = "([{"
    fechamento = ")]}"
    for i in expressao:
        if i in abertura:
            pilha.inserir(i)
        elif i in fechamento:
            if pilha.is_empty():
                return False
            if abertura.index(pilha.topo()) != fechamento.index(i):
                return False
            pilha.remover()
    return pilha.is_empty()


expressao = input('Digite a expressão: ')
if estaBalanceado(expressao):
    print("A expressão está balanceada.")
else:
    print("A expressão não está balanceada.")