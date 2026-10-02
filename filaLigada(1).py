from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class Item:
    ''' Representa um item da fila '''
    valor: str

@dataclass
class No:
    elemento: Item | None
    proximo: No | None = None 


class FilaDinamica():
    ''' Representa uma fila dinamica com sentinela '''

    def __init__(self) -> None:
        ''' Inicializa a fila '''
        self.inicio = No(None)
        self.fim = self.inicio
        self.qtdElem = 0

    def vazia(self) -> bool:
        ''' verifica se a fila está vazia '''
        return self.inicio.proximo == None
    
    def enfileira(self, elem: Item) -> None:
        ''' Insere um elemento na fila '''
        novo = No(elem)
        self.fim.proximo = novo
        self.fim = novo
        self.qtdElem += 1
        
    def desenfileira(self) -> Item:
        ''' Remove um elemento da fila '''
        if self.vazia():
            raise ValueError('Lista vazia')
        removido = self.inicio.proximo
        self.inicio.proximo = removido.proximo
        removido.proximo = None
        self.qtdElem -= 1
        if self.vazia():
            self.fim = self.inicio
        return removido.elemento
    
    def primeiroElemento(self) -> Item:
        ''' Retorna o primeiro elemento da fila '''
        if self.vazia():
            raise ValueError('Fila Vazia')
        return deepcopy(self.inicio.proximo)
        
    def exibe(self) -> None:
     '''Exibe os elementos da fila'''
     p = self.inicio.proximo
     while p != None:
         print(p.elemento.senha)
         p = p.proximo
            
    def esvazia(self) -> None:
      '''Esvazia a fila'''
      while not self.vazia():
          self.desenfileira()
          self.qtdElem = 0
        
    def tamanho(self) -> int:
        '''Retorna o tamanho da fila'''
        return self.qtdElem
    