import pytest

from lista import Lista


class TestListaInicializacao:
    def test_lista_inicia_vazia(self):
        lista = Lista[int](5)

        assert len(lista) == 0
        assert lista.is_empty()

    def test_lista_com_capacidade_um(self):
        lista = Lista[int](1)

        assert len(lista) == 0
        assert lista.is_empty()

    def test_capacidade_invalida(self):
        with pytest.raises((ValueError, AssertionError)):
            Lista[int](0)


class TestListaTamanho:
    def test_size_aumenta_apos_insercao(self):
        lista = Lista[int](5)

        lista.insert(0, 10)
        assert len(lista) == 1

        lista.insert(1, 20)
        assert len(lista) == 2

        lista.insert(2, 30)
        assert len(lista) == 3

    def test_size_diminui_apos_remocao(self):
        lista = Lista[int](5)

        lista.insert(0, 10)
        lista.insert(1, 20)
        lista.insert(2, 30)

        lista.remove(1)

        assert len(lista) == 2

    def test_is_empty_apos_insercao_e_remocao(self):
        lista = Lista[int](5)

        assert lista.is_empty()

        lista.insert(0, 10)
        assert not lista.is_empty()

        lista.remove(0)
        assert lista.is_empty()


class TestListaGetItem:
    def test_acessa_elementos(self):
        lista = Lista[int](5)

        lista.insert(0, 10)
        lista.insert(1, 20)
        lista.insert(2, 30)

        assert lista[0] == 10
        assert lista[1] == 20
        assert lista[2] == 30

    def test_acesso_em_lista_vazia(self):
        lista = Lista[int](5)

        with pytest.raises(IndexError):
            lista[0]

    @pytest.mark.parametrize("posição", [-1, 3, 4, 100])
    def test_acesso_em_posicao_invalida(self, posição):
        lista = Lista[int](5)

        lista.insert(0, 10)
        lista.insert(1, 20)
        lista.insert(2, 30)

        with pytest.raises(IndexError):
            lista[posição]


class TestListaSetItem:
    def test_altera_elemento(self):
        lista = Lista[int](5)

        lista.insert(0, 10)
        lista.insert(1, 20)
        lista.insert(2, 30)

        lista[1] = 25

        assert lista[0] == 10
        assert lista[1] == 25
        assert lista[2] == 30
        assert len(lista) == 3

    @pytest.mark.parametrize("posição", [-1, 3, 100])
    def test_alteracao_em_posicao_invalida(self, posição):
        lista = Lista[int](5)

        lista.insert(0, 10)
        lista.insert(1, 20)
        lista.insert(2, 30)

        with pytest.raises(IndexError):
            lista[posição] = 99


class TestListaFind:
    def test_encontra_elemento(self):
        lista = Lista[int](5)

        lista.insert(0, 10)
        lista.insert(1, 20)
        lista.insert(2, 30)

        assert lista.find(10) == 0
        assert lista.find(20) == 1
        assert lista.find(30) == 2

    def test_elemento_nao_encontrado(self):
        lista = Lista[int](5)

        lista.insert(0, 10)
        lista.insert(1, 20)

        assert lista.find(50) == -1

    def test_find_retorna_primeira_ocorrencia(self):
        lista = Lista[int](5)

        lista.insert(0, 10)
        lista.insert(1, 20)
        lista.insert(2, 10)
        lista.insert(3, 30)

        assert lista.find(10) == 0

    def test_find_nao_altera_lista(self):
        lista = Lista[int](5)

        lista.insert(0, 10)
        lista.insert(1, 20)
        lista.insert(2, 30)

        lista.find(20)

        assert len(lista) == 3
        assert lista[0] == 10
        assert lista[1] == 20
        assert lista[2] == 30


class TestListaInsert:
    def test_insere_em_lista_vazia(self):
        lista = Lista[int](5)

        lista.insert(0, 10)

        assert len(lista) == 1
        assert lista[0] == 10

    def test_insere_no_inicio(self):
        lista = Lista[int](5)

        lista.insert(0, 20)
        lista.insert(0, 10)

        assert lista[0] == 10
        assert lista[1] == 20

    def test_insere_no_meio(self):
        lista = Lista[int](5)

        lista.insert(0, 10)
        lista.insert(1, 30)
        lista.insert(1, 20)

        assert lista[0] == 10
        assert lista[1] == 20
        assert lista[2] == 30

    def test_insere_no_final(self):
        lista = Lista[int](5)

        lista.insert(0, 10)
        lista.insert(1, 20)
        lista.insert(2, 30)

        assert lista[0] == 10
        assert lista[1] == 20
        assert lista[2] == 30

    def test_insercao_preserva_ordem(self):
        lista = Lista[int](10)

        for elemento in [10, 20, 30, 40, 50]:
            lista.insert(len(lista), elemento)

        lista.insert(2, 25)

        assert [lista[i] for i in range(len(lista))] == [
            10, 20, 25, 30, 40, 50
        ]

    @pytest.mark.parametrize("posição", [-1, 4, 10])
    def test_insercao_em_posicao_invalida(self, posição):
        lista = Lista[int](5)

        lista.insert(0, 10)
        lista.insert(1, 20)
        lista.insert(2, 30)

        with pytest.raises(IndexError):
            lista.insert(posição, 99)

        assert len(lista) == 3
        assert [lista[i] for i in range(len(lista))] == [10, 20, 30]


class TestListaRedimensionamento:
    def test_redimensiona_ao_ficar_cheia(self):
        lista = Lista[int](2)

        lista.insert(0, 10)
        lista.insert(1, 20)
        lista.insert(2, 30)

        assert len(lista) == 3
        assert lista[0] == 10
        assert lista[1] == 20
        assert lista[2] == 30

    def test_multiplos_redimensionamentos_preservam_elementos(self):
        lista = Lista[int](2)

        quantidade_elementos = 100

        for elemento in range(quantidade_elementos):
            lista.insert(len(lista), elemento)

        assert len(lista) == quantidade_elementos

        for i in range(quantidade_elementos):
            assert lista[i] == i

    def test_redimensionamento_com_insercao_no_inicio(self):
        lista = Lista[int](2)

        lista.insert(0, 20)
        lista.insert(1, 30)
        lista.insert(0, 10)

        assert [lista[i] for i in range(len(lista))] == [
            10, 20, 30
        ]

    def test_redimensionamento_com_insercao_no_meio(self):
        lista = Lista[int](2)

        lista.insert(0, 10)
        lista.insert(1, 30)
        lista.insert(1, 20)

        assert [lista[i] for i in range(len(lista))] == [
            10, 20, 30
        ]

    def test_multiplas_insercoes_com_redimensionamentos(self):
        lista = Lista[int](2)

        lista.insert(0, 10)
        lista.insert(1, 30)
        lista.insert(1, 20)
        lista.insert(0, 5)
        lista.insert(4, 40)
        lista.insert(2, 15)
        lista.insert(6, 50)
        lista.insert(3, 25)

        assert [lista[i] for i in range(len(lista))] == [
            5, 10, 15, 25, 20, 30, 40, 50
        ]


class TestListaRemove:
    def test_remove_elemento(self):
        lista = Lista[int](5)

        lista.insert(0, 10)
        lista.insert(1, 20)
        lista.insert(2, 30)

        removido = lista.remove(1)

        assert removido == 20
        assert len(lista) == 2
        assert [lista[i] for i in range(len(lista))] == [10, 30]

    def test_remove_primeiro(self):
        lista = Lista[int](5)

        for elemento in [10, 20, 30]:
            lista.insert(len(lista), elemento)

        assert lista.remove(0) == 10
        assert [lista[i] for i in range(len(lista))] == [20, 30]

    def test_remove_ultimo(self):
        lista = Lista[int](5)

        for elemento in [10, 20, 30]:
            lista.insert(len(lista), elemento)

        assert lista.remove(2) == 30
        assert [lista[i] for i in range(len(lista))] == [10, 20]

    def test_remove_unico_elemento(self):
        lista = Lista[int](5)

        lista.insert(0, 10)

        assert lista.remove(0) == 10
        assert lista.is_empty()
        assert len(lista) == 0

    def test_remove_preserva_ordem(self):
        lista = Lista[int](10)

        for elemento in [10, 20, 30, 40, 50]:
            lista.insert(len(lista), elemento)

        lista.remove(2)

        assert [lista[i] for i in range(len(lista))] == [
            10, 20, 40, 50
        ]

    @pytest.mark.parametrize("posição", [-1, 3, 10])
    def test_remocao_em_posicao_invalida(self, posição):
        lista = Lista[int](5)

        lista.insert(0, 10)
        lista.insert(1, 20)
        lista.insert(2, 30)

        with pytest.raises(IndexError):
            lista.remove(posição)

        assert len(lista) == 3
        assert [lista[i] for i in range(len(lista))] == [10, 20, 30]

    def test_remove_em_lista_vazia(self):
        lista = Lista[int](5)

        with pytest.raises(IndexError):
            lista.remove(0)


class TestListaIntegracao:
    def test_sequencia_completa_de_operacoes(self):
        lista = Lista[int](2)

        lista.insert(0, 10)
        lista.insert(1, 20)
        lista.insert(2, 30)
        lista.insert(1, 15)

        assert [lista[i] for i in range(len(lista))] == [
            10, 15, 20, 30
        ]

        assert lista.remove(2) == 20

        lista[1] = 25

        assert lista.find(30) == 2
        assert [lista[i] for i in range(len(lista))] == [
            10, 25, 30
        ]

    def test_lista_com_strings(self):
        lista = Lista[str](2)

        lista.insert(0, "A")
        lista.insert(1, "B")
        lista.insert(1, "X")

        assert [lista[i] for i in range(len(lista))] == [
            "A", "X", "B"
        ]

        lista[1] = "Y"

        assert lista.find("Y") == 1

    def test_lista_com_objetos(self):
        lista = Lista[dict](2)

        primeiro = {"id": 1}
        segundo = {"id": 2}

        lista.insert(0, primeiro)
        lista.insert(1, segundo)

        assert lista[0] is primeiro
        assert lista[1] is segundo