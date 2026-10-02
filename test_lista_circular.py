import pytest

from lista_circular import Lista

class TestListaEncadeamento:
    """
    Testes específicos da implementação baseada em nós duplamente
    encadeados e circulares.

    Esses testes verificam as propriedades internas da estrutura,
    garantindo que os nós estejam corretamente ligados tanto pela
    referência ``proximo`` quanto pela referência ``anterior``, e que
    o encadeamento forme um ciclo.
    """

    def test_lista_vazia_nao_possui_inicio(self):
        lista = Lista[int]()

        assert lista._Lista__inicio is None

    def test_no_unico_aponta_para_si_proprio(self):
        lista = Lista[int]()

        lista.insert(0, 10)

        primeiro = lista._Lista__inicio

        assert primeiro.elemento == 10
        assert primeiro.proximo is primeiro
        assert primeiro.anterior is primeiro

    def test_insercao_no_inicio_atualiza_inicio_e_encadeamento(self):
        lista = Lista[int]()

        lista.insert(0, 10)
        primeiro = lista._Lista__inicio

        lista.insert(0, 20)

        novo_primeiro = lista._Lista__inicio
        ultimo = novo_primeiro.anterior

        assert novo_primeiro is not primeiro
        assert novo_primeiro.elemento == 20
        assert novo_primeiro.proximo is primeiro
        assert primeiro.anterior is novo_primeiro

        assert ultimo is primeiro
        assert ultimo.proximo is novo_primeiro
        assert novo_primeiro.anterior is ultimo

    def test_nos_estao_encadeados_nas_duas_direcoes(self):
        lista = Lista[int]()

        lista.insert(0, 10)
        lista.insert(1, 20)
        lista.insert(2, 30)

        primeiro = lista._Lista__inicio
        segundo = primeiro.proximo
        terceiro = segundo.proximo

        assert primeiro.elemento == 10
        assert segundo.elemento == 20
        assert terceiro.elemento == 30

        # Encadeamento para frente.
        assert primeiro.proximo is segundo
        assert segundo.proximo is terceiro
        assert terceiro.proximo is primeiro

        # Encadeamento para trás.
        assert primeiro.anterior is terceiro
        assert terceiro.anterior is segundo
        assert segundo.anterior is primeiro

    def test_lista_forma_um_ciclo(self):
        lista = Lista[int]()

        lista.insert(0, 10)
        lista.insert(1, 20)
        lista.insert(2, 30)

        primeiro = lista._Lista__inicio

        p = primeiro

        for _ in range(3):
            p = p.proximo

        assert p is primeiro

    def test_lista_forma_um_ciclo_na_direcao_anterior(self):
        lista = Lista[int]()

        lista.insert(0, 10)
        lista.insert(1, 20)
        lista.insert(2, 30)

        primeiro = lista._Lista__inicio

        p = primeiro

        for _ in range(3):
            p = p.anterior

        assert p is primeiro

    def test_relacao_entre_proximo_e_anterior(self):
        lista = Lista[int]()

        lista.insert(0, 10)
        lista.insert(1, 20)
        lista.insert(2, 30)

        primeiro = lista._Lista__inicio
        segundo = primeiro.proximo
        terceiro = segundo.proximo

        assert primeiro.proximo.anterior is primeiro
        assert segundo.proximo.anterior is segundo
        assert terceiro.proximo.anterior is terceiro

        assert primeiro.anterior.proximo is primeiro
        assert segundo.anterior.proximo is segundo
        assert terceiro.anterior.proximo is terceiro

    def test_remocao_no_inicio_atualiza_encadeamento(self):
        lista = Lista[int]()

        lista.insert(0, 10)
        lista.insert(1, 20)
        lista.insert(2, 30)

        primeiro = lista._Lista__inicio
        segundo = primeiro.proximo
        terceiro = segundo.proximo

        lista.remove(0)

        novo_primeiro = lista._Lista__inicio

        assert novo_primeiro is segundo
        assert novo_primeiro.elemento == 20

        assert novo_primeiro.proximo is terceiro
        assert novo_primeiro.anterior is terceiro

        assert terceiro.proximo is novo_primeiro
        assert terceiro.anterior is novo_primeiro

    def test_remocao_no_meio_reconecta_nos_nas_duas_direcoes(self):
        lista = Lista[int]()

        lista.insert(0, 10)
        lista.insert(1, 20)
        lista.insert(2, 30)

        primeiro = lista._Lista__inicio
        segundo = primeiro.proximo
        terceiro = segundo.proximo

        lista.remove(1)

        assert lista._Lista__inicio is primeiro
        assert primeiro.proximo is terceiro
        assert terceiro.anterior is primeiro

        assert terceiro.proximo is primeiro
        assert primeiro.anterior is terceiro

    def test_remocao_no_final_preserva_circularidade(self):
        lista = Lista[int]()

        lista.insert(0, 10)
        lista.insert(1, 20)
        lista.insert(2, 30)

        primeiro = lista._Lista__inicio
        segundo = primeiro.proximo

        lista.remove(2)

        assert lista._Lista__inicio is primeiro
        assert primeiro.proximo is segundo
        assert segundo.proximo is primeiro

        assert primeiro.anterior is segundo
        assert segundo.anterior is primeiro

    def test_remocao_do_unico_no_deixa_lista_vazia(self):
        lista = Lista[int]()

        lista.insert(0, 10)

        no = lista._Lista__inicio

        lista.remove(0)

        assert lista._Lista__inicio is None
        assert len(lista) == 0

        # O nó removido não faz mais parte da lista.
        assert no.proximo is no
        assert no.anterior is no
