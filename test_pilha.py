import pytest

from pilha import Pilha


def test_pilha_nova_esta_vazia() -> None:
    pilha = Pilha[int](5)

    assert pilha.is_empty()


def test_pilha_nova_nao_esta_cheia() -> None:
    pilha = Pilha[int](5)

    assert not pilha.is_full()


def test_capacidade_um() -> None:
    pilha = Pilha[int](1)

    assert pilha.is_empty()
    assert not pilha.is_full()

    pilha.push(10)

    assert not pilha.is_empty()
    assert pilha.is_full()
    assert pilha.top() == 10
    assert pilha.pop() == 10

    assert pilha.is_empty()
    assert not pilha.is_full()


def test_capacidade_invalida() -> None:
    with pytest.raises(ValueError):
        Pilha[int](0)

    with pytest.raises(ValueError):
        Pilha[int](-1)


def test_is_empty_muda_apos_push() -> None:
    pilha = Pilha[int](5)

    assert pilha.is_empty()

    pilha.push(10)

    assert not pilha.is_empty()


def test_is_empty_muda_apos_pop() -> None:
    pilha = Pilha[int](5)

    pilha.push(10)

    assert not pilha.is_empty()

    pilha.pop()

    assert pilha.is_empty()


def test_is_full_muda_ao_atingir_capacidade() -> None:
    pilha = Pilha[int](3)

    assert not pilha.is_full()

    pilha.push(10)
    assert not pilha.is_full()

    pilha.push(20)
    assert not pilha.is_full()

    pilha.push(30)
    assert pilha.is_full()


def test_is_full_deixa_de_ser_verdade_apos_pop() -> None:
    pilha = Pilha[int](2)

    pilha.push(10)
    pilha.push(20)

    assert pilha.is_full()

    pilha.pop()

    assert not pilha.is_full()


def test_push_insere_elemento() -> None:
    pilha = Pilha[int](5)

    pilha.push(10)

    assert pilha.top() == 10


def test_push_coloca_novo_elemento_no_topo() -> None:
    pilha = Pilha[int](5)

    pilha.push(10)
    pilha.push(20)
    pilha.push(30)

    assert pilha.top() == 30


def test_top_retorna_elemento_do_topo() -> None:
    pilha = Pilha[int](5)

    pilha.push(10)
    pilha.push(20)
    pilha.push(30)

    assert pilha.top() == 30


def test_top_nao_remove_elemento() -> None:
    pilha = Pilha[int](5)

    pilha.push(10)
    pilha.push(20)

    assert pilha.top() == 20
    assert pilha.top() == 20
    assert pilha.top() == 20

    assert pilha.pop() == 20


def test_pop_retorna_elemento_do_topo() -> None:
    pilha = Pilha[int](5)

    pilha.push(10)
    pilha.push(20)

    assert pilha.pop() == 20


def test_pop_remove_elemento() -> None:
    pilha = Pilha[int](5)

    pilha.push(10)
    pilha.push(20)

    pilha.pop()

    assert pilha.top() == 10


def test_pop_respeita_lifo() -> None:
    pilha = Pilha[str](5)

    pilha.push("A")
    pilha.push("B")
    pilha.push("C")

    assert pilha.pop() == "C"
    assert pilha.pop() == "B"
    assert pilha.pop() == "A"


def test_pilha_fica_vazia_apos_remover_todos_os_elementos() -> None:
    pilha = Pilha[int](3)

    pilha.push(10)
    pilha.push(20)
    pilha.push(30)

    pilha.pop()
    pilha.pop()
    pilha.pop()

    assert pilha.is_empty()


def test_pilha_pode_ser_reutilizada_apos_esvaziada() -> None:
    pilha = Pilha[int](3)

    pilha.push(10)
    pilha.push(20)

    assert pilha.pop() == 20
    assert pilha.pop() == 10
    assert pilha.is_empty()

    pilha.push(30)

    assert not pilha.is_empty()
    assert pilha.top() == 30
    assert pilha.pop() == 30
    assert pilha.is_empty()


def test_push_em_pilha_cheia_produz_overflow_error() -> None:
    pilha = Pilha[int](2)

    pilha.push(10)
    pilha.push(20)

    with pytest.raises(OverflowError):
        pilha.push(30)


def test_push_em_pilha_cheia_nao_altera_o_estado() -> None:
    pilha = Pilha[int](2)

    pilha.push(10)
    pilha.push(20)

    with pytest.raises(OverflowError):
        pilha.push(30)

    assert pilha.is_full()
    assert pilha.top() == 20
    assert pilha.pop() == 20
    assert pilha.pop() == 10


def test_pop_em_pilha_vazia_produz_index_error() -> None:
    pilha = Pilha[int](5)

    with pytest.raises(IndexError):
        pilha.pop()


def test_pop_em_pilha_vazia_nao_altera_o_estado() -> None:
    pilha = Pilha[int](5)

    with pytest.raises(IndexError):
        pilha.pop()

    assert pilha.is_empty()
    assert not pilha.is_full()


def test_top_em_pilha_vazia_produz_index_error() -> None:
    pilha = Pilha[int](5)

    with pytest.raises(IndexError):
        pilha.top()


def test_top_em_pilha_vazia_nao_altera_o_estado() -> None:
    pilha = Pilha[int](5)

    with pytest.raises(IndexError):
        pilha.top()

    assert pilha.is_empty()
    assert not pilha.is_full()


def test_top_e_pop_produzem_o_mesmo_elemento() -> None:
    pilha = Pilha[int](5)

    pilha.push(10)
    pilha.push(20)
    pilha.push(30)

    assert pilha.top() == pilha.pop()

    assert pilha.top() == 20


def test_sequencia_de_operacoes() -> None:
    pilha = Pilha[int](5)

    pilha.push(10)
    pilha.push(20)
    pilha.push(30)

    assert pilha.top() == 30
    assert pilha.pop() == 30

    pilha.push(40)

    assert pilha.top() == 40
    assert pilha.pop() == 40
    assert pilha.pop() == 20
    assert pilha.pop() == 10

    assert pilha.is_empty()


def test_push_pop_intercalados() -> None:
    pilha = Pilha[int](4)

    pilha.push(1)
    assert pilha.pop() == 1

    pilha.push(2)
    pilha.push(3)
    assert pilha.pop() == 3

    pilha.push(4)
    pilha.push(5)

    assert pilha.pop() == 5
    assert pilha.pop() == 4
    assert pilha.pop() == 2

    assert pilha.is_empty()


def test_pilha_preserva_elementos_de_tipos_distintos_de_valor_concreto() -> None:
    pilha = Pilha[str](3)

    pilha.push("primeiro")
    pilha.push("segundo")
    pilha.push("terceiro")

    assert pilha.pop() == "terceiro"
    assert pilha.pop() == "segundo"
    assert pilha.pop() == "primeiro"


def test_pilha_chega_a_capacidade_maxima_e_depois_e_esvaziada() -> None:
    pilha = Pilha[int](5)

    for valor in range(5):
        pilha.push(valor)

    assert pilha.is_full()

    for valor in range(4, -1, -1):
        assert pilha.pop() == valor

    assert pilha.is_empty()