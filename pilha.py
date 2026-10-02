#Modifique o método desempilha() da classe PilhaEstatica para que ele retorne o elemento desempilhado

from dataclasses import dataclass
from copy import deepcopy
from vetor import Vetor

@dataclass
class Item:
    """Representa um item da pilha."""
    valor: str


class PilhaEstatica():
    """Representa uma pilha estática."""

    def __init__(self, tam_max: int) -> None:
        self.TAM_MAX = tam_max
        self.elementos = Vetor(tam_max)
        self.topo = 0

    def vazia(self) -> bool:
        return self.topo == 0
    
    def cheia(self) -> bool:
        return self.topo == self.TAM_MAX

    def empilha(self, elem: Item) -> None:
        if self.cheia():
            raise ValueError('Pilha Cheia')
        self.elementos[self.topo] = deepcopy(elem)
        self.topo += 1

    def desempilha(self) -> Item:
        if self.vazia():
            raise ValueError('Pilha Vazia')
        self.topo -=1
        return deepcopy(self.elementos[self.topo])
    
    def elementoTopo(self) -> Item:
        if self.vazia():
            raise ValueError('Pilha Vazia')
        return deepcopy(self.elementos[self.topo-1])
        
    def exibe(self) -> None:
        print('Pilha: [', end='')
        for i in range(self.topo):
            print(self.elementos[i], end='')
            if i < self.topo - 1:
                print(', ', end='')
        print('] <-- topo')
            
    def esvazia(self) -> None:
        self.topo = 0