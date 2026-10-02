import random
import time

from arranjo import Arranjo
from ordenacao import insertion_sort, merge_sort


# ============================================================
# Funções auxiliares
# ============================================================

def criar_arranjo(valores):
    A = Arranjo(len(valores))

    for i in range(len(valores)):
        A[i] = valores[i]

    return A


def para_lista(A):
    valores = []

    for i in range(len(A)):
        valores.append(A[i])

    return valores


# ============================================================
# 1. Testes de correção
# ============================================================

def testar_correcao():
    casos = [
        [1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [4, 1, 7, 3, 6, 2, 5],
        [5, 5, 2, 2, 8, 1, 1],
        [-3, 5, 0, -1, 8, 2],
    ]

    print("=== TESTE DE CORREÇÃO ===")

    for caso in casos:
        esperado = sorted(caso)

        # Insertion Sort
        A = criar_arranjo(caso)
        insertion_sort(A)

        obtido = para_lista(A)

        if obtido != esperado:
            print("ERRO - Insertion Sort")
            print("Entrada :", caso)
            print("Obtido   :", obtido)
            print("Esperado :", esperado)
            return

        # Mergesort
        A = criar_arranjo(caso)
        merge_sort(A, 0, len(A) - 1)

        obtido = para_lista(A)

        if obtido != esperado:
            print("ERRO - Mergesort")
            print("Entrada :", caso)
            print("Obtido   :", obtido)
            print("Esperado :", esperado)
            return

    print("Todos os testes passaram!")
    print()


# ============================================================
# 2. Teste visual
# ============================================================

def teste_visual():
    valores = [7, 3, 9, 2, 5, 1, 8, 4]

    print("=== TESTE VISUAL ===")
    print("Entrada:       ", valores)

    # Insertion Sort
    A = criar_arranjo(valores)
    insertion_sort(A)
    print("Insertion Sort:", para_lista(A))

    # Mergesort
    A = criar_arranjo(valores)
    merge_sort(A, 0, len(A) - 1)
    print("Mergesort:     ", para_lista(A))

    print()


# ============================================================
# 3. Comparação de tempo
# ============================================================

def comparar_tempos():
    tamanhos = [100, 500, 1000, 5000, 10000]

    print("=== COMPARAÇÃO DE TEMPO ===")
    print()
    print(f"{'n':>8} {'Insertion':>15} {'Mergesort':>15}")
    print("-" * 42)

    for n in tamanhos:

        # Gera uma entrada aleatória
        valores = list(range(n))
        random.shuffle(valores)

        # Insertion Sort
        A = criar_arranjo(valores)

        inicio = time.perf_counter()
        insertion_sort(A)
        tempo_insertion = time.perf_counter() - inicio

        # Mergesort
        A = criar_arranjo(valores)

        inicio = time.perf_counter()
        merge_sort(A, 0, len(A) - 1)
        tempo_merge = time.perf_counter() - inicio

        print(
            f"{n:>8} "
            f"{tempo_insertion:>15.6f} "
            f"{tempo_merge:>15.6f}"
        )

    print()


# ============================================================
# 4. Comparação de diferentes tipos de entrada
# ============================================================

def comparar_entradas(n):
    entradas = {
        "Ordenada": list(range(n)),
        "Inversa": list(range(n, 0, -1)),
        "Aleatória": random.sample(range(n), n)
    }

    print(f"=== ENTRADAS COM n = {n} ===")
    print()
    print(f"{'Entrada':<15} {'Insertion':>15} {'Mergesort':>15}")
    print("-" * 48)

    for nome, valores in entradas.items():

        # Insertion Sort
        A = criar_arranjo(valores)

        inicio = time.perf_counter()
        insertion_sort(A)
        tempo_insertion = time.perf_counter() - inicio

        # Mergesort
        A = criar_arranjo(valores)

        inicio = time.perf_counter()
        merge_sort(A, 0, len(A) - 1)
        tempo_merge = time.perf_counter() - inicio

        print(
            f"{nome:<15} "
            f"{tempo_insertion:>15.6f} "
            f"{tempo_merge:>15.6f}"
        )

    print()


# ============================================================
# Programa principal
# ============================================================

if __name__ == "__main__":

    testar_correcao()

    teste_visual()

    comparar_tempos()

    comparar_entradas(10000)