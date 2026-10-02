import pytest

from fila import Fila


def test_fila_nova_esta_vazia() -> None:
    fila = Fila[int](5)

    assert fila.is_empty()


def test_fila_nova_nao_esta_cheia() -> None:
    fila = Fila[int](5)

    assert not fila.is_full()


def test_capacidade_um() -> None:
    fila = Fila[int](1)

    assert fila.is_empty()
    assert not fila.is_full()

    fila.enqueue(10)

    assert not fila.is_empty()
    assert fila.is_full()
    assert fila.front() == 10
    assert fila.dequeue() == 10

    assert fila.is_empty()
    assert not fila.is_full()


def test_capacidade_invalida() -> None:
    with pytest.raises(ValueError):
        Fila[int](0)

    with pytest.raises(ValueError):
        Fila[int](-1)


def test_is_empty_muda_apos_enqueue() -> None:
    fila = Fila[int](5)

    assert fila.is_empty()

    fila.enqueue(10)

    assert not fila.is_empty()


def test_is_empty_muda_apos_dequeue() -> None:
    fila = Fila[int](5)

    fila.enqueue(10)

    assert not fila.is_empty()

    fila.dequeue()

    assert fila.is_empty()


def test_is_full_muda_ao_atingir_capacidade() -> None:
    fila = Fila[int](3)

    assert not fila.is_full()

    fila.enqueue(10)
    assert not fila.is_full()

    fila.enqueue(20)
    assert not fila.is_full()

    fila.enqueue(30)
    assert fila.is_full()


def test_is_full_deixa_de_ser_verdade_apos_dequeue() -> None:
    fila = Fila[int](2)

    fila.enqueue(10)
    fila.enqueue(20)

    assert fila.is_full()

    fila.dequeue()

    assert not fila.is_full()


def test_enqueue_insere_elemento() -> None:
    fila = Fila[int](5)

    fila.enqueue(10)

    assert fila.front() == 10


def test_enqueue_coloca_novo_elemento_no_final() -> None:
    fila = Fila[str](5)

    fila.enqueue("A")
    fila.enqueue("B")
    fila.enqueue("C")

    assert fila.dequeue() == "A"
    assert fila.dequeue() == "B"
    assert fila.dequeue() == "C"


def test_front_retorna_primeiro_elemento() -> None:
    fila = Fila[int](5)

    fila.enqueue(10)
    fila.enqueue(20)
    fila.enqueue(30)

    assert fila.front() == 10


def test_front_nao_remove_elemento() -> None:
    fila = Fila[int](5)

    fila.enqueue(10)
    fila.enqueue(20)

    assert fila.front() == 10
    assert fila.front() == 10
    assert fila.front() == 10

    assert fila.dequeue() == 10


def test_dequeue_retorna_primeiro_elemento() -> None:
    fila = Fila[int](5)

    fila.enqueue(10)
    fila.enqueue(20)

    assert fila.dequeue() == 10


def test_dequeue_remove_primeiro_elemento() -> None:
    fila = Fila[int](5)

    fila.enqueue(10)
    fila.enqueue(20)

    fila.dequeue()

    assert fila.front() == 20


def test_dequeue_respeita_fifo() -> None:
    fila = Fila[str](5)

    fila.enqueue("A")
    fila.enqueue("B")
    fila.enqueue("C")

    assert fila.dequeue() == "A"
    assert fila.dequeue() == "B"
    assert fila.dequeue() == "C"


def test_fila_fica_vazia_apos_remover_todos_os_elementos() -> None:
    fila = Fila[int](3)

    fila.enqueue(10)
    fila.enqueue(20)
    fila.enqueue(30)

    fila.dequeue()
    fila.dequeue()
    fila.dequeue()

    assert fila.is_empty()


def test_fila_pode_ser_reutilizada_apos_esvaziada() -> None:
    fila = Fila[int](3)

    fila.enqueue(10)
    fila.enqueue(20)

    assert fila.dequeue() == 10
    assert fila.dequeue() == 20
    assert fila.is_empty()

    fila.enqueue(30)

    assert not fila.is_empty()
    assert fila.front() == 30
    assert fila.dequeue() == 30
    assert fila.is_empty()


def test_enqueue_em_fila_cheia_produz_overflow_error() -> None:
    fila = Fila[int](2)

    fila.enqueue(10)
    fila.enqueue(20)

    with pytest.raises(OverflowError):
        fila.enqueue(30)


def test_enqueue_em_fila_cheia_nao_altera_o_estado() -> None:
    fila = Fila[int](2)

    fila.enqueue(10)
    fila.enqueue(20)

    with pytest.raises(OverflowError):
        fila.enqueue(30)

    assert fila.is_full()
    assert fila.front() == 10
    assert fila.dequeue() == 10
    assert fila.dequeue() == 20


def test_dequeue_em_fila_vazia_produz_index_error() -> None:
    fila = Fila[int](5)

    with pytest.raises(IndexError):
        fila.dequeue()


def test_dequeue_em_fila_vazia_nao_altera_o_estado() -> None:
    fila = Fila[int](5)

    with pytest.raises(IndexError):
        fila.dequeue()

    assert fila.is_empty()
    assert not fila.is_full()


def test_front_em_fila_vazia_produz_index_error() -> None:
    fila = Fila[int](5)

    with pytest.raises(IndexError):
        fila.front()


def test_front_em_fila_vazia_nao_altera_o_estado() -> None:
    fila = Fila[int](5)

    with pytest.raises(IndexError):
        fila.front()

    assert fila.is_empty()
    assert not fila.is_full()


def test_front_e_dequeue_produzem_o_mesmo_elemento() -> None:
    fila = Fila[int](5)

    fila.enqueue(10)
    fila.enqueue(20)
    fila.enqueue(30)

    assert fila.front() == fila.dequeue()

    assert fila.front() == 20


def test_sequencia_de_operacoes() -> None:
    fila = Fila[int](5)

    fila.enqueue(10)
    fila.enqueue(20)
    fila.enqueue(30)

    assert fila.front() == 10
    assert fila.dequeue() == 10

    fila.enqueue(40)

    assert fila.front() == 20
    assert fila.dequeue() == 20
    assert fila.dequeue() == 30
    assert fila.dequeue() == 40

    assert fila.is_empty()


def test_enqueue_dequeue_intercalados() -> None:
    fila = Fila[int](4)

    fila.enqueue(1)
    assert fila.dequeue() == 1

    fila.enqueue(2)
    fila.enqueue(3)
    assert fila.dequeue() == 2

    fila.enqueue(4)
    fila.enqueue(5)

    assert fila.dequeue() == 3
    assert fila.dequeue() == 4
    assert fila.dequeue() == 5

    assert fila.is_empty()


def test_reutiliza_posicoes_liberadas() -> None:
    fila = Fila[str](3)

    fila.enqueue("A")
    fila.enqueue("B")
    fila.enqueue("C")

    assert fila.dequeue() == "A"
    assert fila.dequeue() == "B"

    fila.enqueue("D")
    fila.enqueue("E")

    assert fila.dequeue() == "C"
    assert fila.dequeue() == "D"
    assert fila.dequeue() == "E"

    assert fila.is_empty()


def test_reutiliza_posicoes_apos_volta_ao_inicio() -> None:
    fila = Fila[int](3)

    fila.enqueue(1)
    fila.enqueue(2)
    fila.enqueue(3)

    assert fila.dequeue() == 1

    fila.enqueue(4)

    assert fila.dequeue() == 2

    fila.enqueue(5)

    assert fila.dequeue() == 3
    assert fila.dequeue() == 4
    assert fila.dequeue() == 5

    assert fila.is_empty()


def test_fila_circular_com_varias_voltas() -> None:
    fila = Fila[int](3)

    for i in range(10):
        fila.enqueue(i)
        assert fila.dequeue() == i

    assert fila.is_empty()


def test_fila_circular_com_fila_parcial() -> None:
    fila = Fila[int](4)

    fila.enqueue(1)
    fila.enqueue(2)
    fila.enqueue(3)

    assert fila.dequeue() == 1

    fila.enqueue(4)
    fila.enqueue(5)

    assert fila.dequeue() == 2
    assert fila.dequeue() == 3
    assert fila.dequeue() == 4
    assert fila.dequeue() == 5

    assert fila.is_empty()


def test_fila_atinge_capacidade_maxima_e_depois_e_esvaziada() -> None:
    fila = Fila[int](5)

    for valor in range(5):
        fila.enqueue(valor)

    assert fila.is_full()

    for valor in range(5):
        assert fila.dequeue() == valor

    assert fila.is_empty()


def test_fila_preserva_ordem_apos_remocoes_e_novas_insercoes() -> None:
    fila = Fila[str](5)

    fila.enqueue("A")
    fila.enqueue("B")
    fila.enqueue("C")

    assert fila.dequeue() == "A"

    fila.enqueue("D")
    fila.enqueue("E")

    assert fila.dequeue() == "B"
    assert fila.dequeue() == "C"
    assert fila.dequeue() == "D"
    assert fila.dequeue() == "E"

    assert fila.is_empty()