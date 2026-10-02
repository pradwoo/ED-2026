from dataclasses import dataclass
from copy import deepcopy
from vetor import Vetor

@dataclass
class Item:
    ''' Representa um item da lista '''
    valor: str


class ListaEstatica():
    ''' Representa uma lista estática '''

    def __init__(self, tamMax: int) -> None:
        ''' Inicializa a lista '''
        self.TAM_MAX = tamMax
        self.elementos = Vetor(tamMax)
        self.fim = 0

    def tamanho(self) -> int:
        ''' Retorna o tamanhho lógico da lista '''
        return self.fim
    
    def vazia(self) -> bool:
        ''' verifica se a lista está vazia '''
        return self.fim == 0
    
    def cheia(self) -> bool:
        ''' verifica se a lista está cheia '''
        return self.fim == self.TAM_MAX
        
    def primeiro(self) -> Item:
        ''' Retorna o primeiro elemento da lista '''
        if self.vazia():
            raise ValueError('Fila Vazia')
        return deepcopy(self.elementos[0])
    
    def ultimo(self) -> Item:
        ''' Retorna o ultimo elemento da lista '''
        if self.vazia():
            raise ValueError('Fila Vazia')
        return deepcopy(self.elementos[self.fim - 1])
        
    def exibe(self) -> None:
        ''' Imprime a lista '''
        print('Lista: inicio --> [', end='')
        for i in range(self.fim):
            print(self.elementos[i].valor, end='')
            if i < self.fim - 1:
                print(', ', end='')
        print('] <-- fim')
            
    def esvazia(self) -> None:
        ''' Esvazia a lista (remove todos os elementos)'''
        self.fim = 0
    
    def busca(self, elem: Item) -> int:
        ''' Faz uma busca sequencial por *elem* e retorna sua posicao '''
        for i in range(self.fim):
            if self.elementos[i].valor == elem.valor:
                return i
        return -1
    
    def buscaPos(self, pos) -> Item:
        ''' Retorna o elemento da posição *pos* '''
        if self.vazia():
            raise ValueError('Lista Vazia')
        if pos < 0 or pos >= self.TAM_MAX:
            raise ValueError('Índice Fora do Limite')
        if pos >= self.fim:
            raise ValueError('Posição inválida')
        return deepcopy(self.elementos[pos])

    def insere(self, elem: Item) -> None:
        ''' Insere elemento no fim da lista - não permite elementos repetidos '''
        if self.cheia():
            raise ValueError('Lista Cheia')
        
        if self.busca(elem) >= 0:
            raise ValueError('Elemento Repetido')

        self.elementos[self.fim] = deepcopy(elem)
        self.fim += 1

    def _deslocaDireita(self, pos: int):
        ''' Função auxiliar: desloca elementos para a direita uma posição '''
        for i in range(self.fim, pos, -1):
            self.elementos[i] = self.elementos[i - 1]

    def inserePos(self, elem: Item, pos: int) -> None:
        ''' Insere elemento na posição *pos* da lista '''
        if self.cheia():
            raise ValueError('Lista Cheia')
        
        if self.busca(elem) >= 0:
            raise ValueError('Elemento Repetido')
        
        if pos < 0 or pos >= self.TAM_MAX:
            raise ValueError('Índice Fora do Limite')
        
        if pos > self.fim:
            raise ValueError('Posição inválida')
        
        self._deslocaDireita(pos)
        
        self.elementos[pos] = deepcopy(elem)
        self.fim += 1

    def remove(self) -> None:
        ''' Remove o elemento do fim da lista '''
        if self.vazia():
            raise ValueError('Lista Vazia')
        self.fim -= 1

    def _deslocaEsquerda(self, pos: int):
        ''' Função auxiliar: desloca elementos para a esquerda uma posição '''
        for i in range(pos + 1, self.fim):
            self.elementos[i - 1] = self.elementos[i]

    def removePos(self, pos: int) -> None:
        ''' Remove o elemento da posição *pos* da lista '''
        if self.vazia():
            raise ValueError('Lista Vazia')
        if pos < 0 or pos >= self.TAM_MAX:
            raise ValueError('Índice Fora do Limite')
        if pos >= self.fim:
            raise ValueError('Posição inválida')
        
        self._deslocaEsquerda(pos)
        self.fim -= 1

    def removeElemento(self, elem: Item) -> None:
        ''' Remove o elemento *elem* da lista '''
        if self.vazia():
            raise ValueError('Lista Vazia')
        posElem = self.busca(elem)
        if posElem == -1:
            raise ValueError('Elemento Inexistente')
        self._deslocaEsquerda(posElem)
        self.fim -= 1
