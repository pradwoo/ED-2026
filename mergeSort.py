from math import inf

def mergeSort(S: list):  

    def merge(S: list, ini: int, meio: int, fim: int):
        # separe as sequências
        s1 = S[ini:meio+1]
        s2 = S[meio+1:fim+1]
        # adicione as sentinelas
        s1.append(inf)
        s2.append(inf)
        # intercale s1 e s2 em S
        i, j, k = 0, 0, ini
        while (k <= fim):
            if s1[i] <= s2[j]:
                S[k] = s1[i]
                i += 1
            else:
                S[k] = s2[j]
                j += 1
            k += 1


    def msort(S: list, ini: int, fim: int):
        meio = (ini + fim) // 2
        if ini < fim:
            msort(S, ini, meio)
            msort(S, meio + 1, fim)
            merge(S, ini, meio, fim)

    msort(S, 0, len(S)-1)

# Ilustre a execução do algoritmo mergeSort para a sequência de valores: E, D, B, H, G, A, F, C

def main():
    S = ['E', 'D', 'B', 'H', 'G', 'A', 'F', 'C']  # Keeping the original input
    print(S)
    mergeSort(S)
    print(S)
    return 0
	
if __name__ == "__main__":
    main()
