from dataclasses import dataclass
from copy import deepcopy
from vetor import Vetor

@dataclass
class Item:
    ''' Representa um item da fila '''
    valor: str


class FilaEstatica():
    ''' Representa uma fila estática '''

    def __init__(self, tamMax: int) -> None:
        ''' Inicializa a fila '''
        self.TAM_MAX = tamMax
        self.elementos = Vetor(tamMax)
        self.qtdElem = 0
        self.inicio = 0
        self.fim = 0

    def vazia(self) -> bool:
        ''' verifica se a fila está vazia '''
        return self.qtdElem == 0
    
    def cheia(self) -> bool:
        ''' verifica se a fila está cheia '''
        return self.qtdElem == self.TAM_MAX
    
    def _avanca(self, indice: int) -> int:
        ''' FUNÇÃO AUXILIAR - retorna o próximo índice de um vetor circular '''
        return (indice + 1) % self.TAM_MAX
           
    def enfileira(self, elem: Item) -> None:
        ''' Insere um elemento na fila '''
        if self.cheia():
            raise ValueError('Fila Cheia')
        self.elementos[self.fim] = deepcopy(elem)
        self.fim = self._avanca(self.fim)
        self.qtdElem += 1
        
    def desenfileira(self) -> Item:
        ''' Remove um elemento da fila '''
        if self.vazia():
            raise ValueError('Fila Vazia')
        elem = self.elementos[self.inicio]
        self.inicio = self._avanca(self.inicio)
        self.qtdElem -= 1
        return elem
    
    def primeiroElemento(self) -> Item:
        ''' Retorna o primeiro elemento da fila '''
        if self.vazia():
            raise ValueError('Fila Vazia')
        return deepcopy(self.elementos[self.inicio])
        
    def exibe(self) -> None:
        ''' Imprime a fila '''
        print('Fila: inicio --> [', end='')
        i = self.inicio
        for k in range(self.qtdElem):
            print(self.elementos[i].valor, end='')
            if k < self.qtdElem - 1:
                print(', ', end='')
            i = self._avanca(i)
        print('] <-- fim')
            
    def esvazia(self) -> None:
        ''' Esvazia a fila (remove todos os elementos)'''
        self.qtdElem = 0
        self.inicio = 0
        self.fim = 0

    def tamanho(self) -> int:
        ''' Retorna o tamanhho lógico da fila '''
        return self.qtdElem
