from typing import Generic, TypeVar

from arranjo import Arranjo


T = TypeVar("T")


class Lista(Generic[T]):
    """
    Representa uma Lista implementada utilizando um arranjo dinâmico.

    A Lista representa uma sequência ordenada de elementos, permitindo
    acesso, alteração, busca, inserção e remoção em diferentes posições.

    A representação utiliza um arranjo cuja capacidade pode ser aumentada
    quando necessário.
    """

    __dados: Arranjo[T]
    __quantidade: int

    def __init__(self, capacidade: int) -> None:
        """
        Cria uma Lista vazia com a capacidade inicial informada.

        Parâmetros
        ----------
        capacidade
            Capacidade inicial do arranjo.

        Pré-condição
        ------------
        ``capacidade > 0``

        Pós-condição
        ------------
        A Lista está vazia e possui a capacidade inicial informada.

        Exemplos
        --------
        >>> lista = Lista[int](5)
        >>> lista.is_empty()
        True
        >>> len(lista)
        0
        """
        self.__dados = Arranjo[T](capacidade)
        self.__quantidade = 0

    def __len__(self) -> int:
        """
        Retorna a quantidade de elementos da Lista.

        Retorna
        -------
        int
            Número de elementos armazenados na Lista.

        Pós-condição
        ------------
        O estado da Lista permanece inalterado.

        Exemplos
        --------
        >>> lista = Lista[int](5)
        >>> len(lista)
        0

        >>> lista.insert(0, 10)
        >>> lista.insert(1, 20)
        >>> len(lista)
        2
        """
        pass

    def is_empty(self) -> bool:
        """
        Verifica se a Lista está vazia.

        Retorna
        -------
        bool
            ``True`` se a Lista estiver vazia e ``False`` caso contrário.

        Pós-condição
        ------------
        O estado da Lista permanece inalterado.

        Exemplos
        --------
        >>> lista = Lista[int](5)
        >>> lista.is_empty()
        True

        >>> lista.insert(0, 10)
        >>> lista.is_empty()
        False
        """
        pass

    def __getitem__(self, posição: int) -> T:
        """
        Retorna o elemento armazenado na posição informada.

        Parâmetros
        ----------
        posição
            Posição do elemento na Lista.

        Retorna
        -------
        T
            Elemento armazenado na posição.

        Pré-condição
        ------------
        ``0 <= posição < size()``

        Levanta
        -------
        IndexError
            Se a posição for inválida.

        Exemplos
        --------
        >>> lista = Lista[int](5)
        >>> lista.insert(0, 10)
        >>> lista.insert(1, 20)
        >>> lista.insert(2, 30)
        >>> lista[1]
        20

        >>> lista[3]
        Traceback (most recent call last):
        ...
        IndexError: posição inválida
        """
        pass

    def __setitem__(self, posição: int, elemento: T) -> None:
        """
        Substitui o elemento armazenado na posição informada.

        Parâmetros
        ----------
        posição
            Posição do elemento que será substituído.
        elemento
            Novo elemento.

        Pré-condição
        ------------
        ``0 <= posição < size()``

        Pós-condição
        ------------
        O elemento na posição informada foi substituído.

        Levanta
        -------
        IndexError
            Se a posição for inválida.

        Exemplos
        --------
        >>> lista = Lista[int](5)
        >>> lista.insert(0, 10)
        >>> lista.insert(1, 20)
        >>> lista[1] = 25
        >>> lista[1]
        25
        """
        pass

    def find(self, elemento: T) -> int:
        """
        Procura um elemento na Lista.

        Parâmetros
        ----------
        elemento
            Elemento procurado.

        Retorna
        -------
        int
            Posição da primeira ocorrência do elemento.
            Retorna ``-1`` se o elemento não estiver na Lista.

        Pós-condição
        ------------
        O estado da Lista permanece inalterado.

        Exemplos
        --------
        >>> lista = Lista[int](5)
        >>> lista.insert(0, 10)
        >>> lista.insert(1, 20)
        >>> lista.insert(2, 30)
        >>> lista.find(20)
        1
        >>> lista.find(50)
        -1
        """
        pass

    def insert(self, posição: int, elemento: T) -> None:
        """
        Insere um elemento na posição informada.

        Os elementos a partir da posição de inserção são deslocados
        uma posição para a direita.

        Parâmetros
        ----------
        posição
            Posição na qual o elemento será inserido.
        elemento
            Elemento a ser inserido.

        Pré-condição
        ------------
        ``0 <= posição <= size()``

        Pós-condição
        ------------
        O elemento passa a ocupar a posição informada.
        A quantidade de elementos aumenta em uma unidade.

        Levanta
        -------
        IndexError
            Se a posição for inválida.

        Exemplos
        --------
        >>> lista = Lista[str](5)
        >>> lista.insert(0, "A")
        >>> lista.insert(1, "B")
        >>> lista.insert(2, "D")
        >>> lista.insert(2, "C")
        >>> lista[0]
        'A'
        >>> lista[1]
        'B'
        >>> lista[2]
        'C'
        >>> lista[3]
        'D'

        >>> lista.insert(5, "X")
        Traceback (most recent call last):
        ...
        IndexError: posição inválida
        """
        pass

    def remove(self, posição: int) -> T:
        """
        Remove e retorna o elemento da posição informada.

        Os elementos posteriores à posição são deslocados
        uma posição para a esquerda.

        Parâmetros
        ----------
        posição
            Posição do elemento que será removido.

        Retorna
        -------
        T
            Elemento removido.

        Pré-condição
        ------------
        ``0 <= posição < size()``

        Pós-condição
        ------------
        O elemento da posição informada foi removido.
        A quantidade de elementos diminui em uma unidade.

        Levanta
        -------
        IndexError
            Se a posição for inválida.

        Exemplos
        --------
        >>> lista = Lista[str](5)
        >>> lista.insert(0, "A")
        >>> lista.insert(1, "B")
        >>> lista.insert(2, "C")
        >>> lista.remove(1)
        'B'
        >>> lista[0]
        'A'
        >>> lista[1]
        'C'

        >>> lista.remove(2)
        Traceback (most recent call last):
        ...
        IndexError: posição inválida
        """
        pass

    def __redimensionar(self, nova_capacidade: int) -> None:
        """
        Redimensiona o arranjo utilizado pela Lista.

        Os elementos existentes são copiados para um novo arranjo.

        Parâmetros
        ----------
        nova_capacidade
            Nova capacidade do arranjo.

        Pré-condição
        ------------
        ``nova_capacidade >= size()``

        Pós-condição
        ------------
        Todos os elementos da Lista são preservados e a capacidade
        passa a ser ``nova_capacidade``.
        """
        pass