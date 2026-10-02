def selectionSort(l: list, n: int) -> None:
	for i in range(n-1):
		# encontra o menor
		id_menor = i
		for j in range(i+1, n):
			if l[j] < l[id_menor]:
				id_menor = j
		# troca
		# aux = l[i]
		# l[i] = l[id_menor]
		# l[id_menor] = aux
		l[i], l[id_menor] = l[id_menor], l[i]


def insertionSort(l: list, n: int) -> None:
	for i in range(1, n):
		aux = l[i]
		j = i
		while j > 0 and l[j-1] > aux:
			l[j] = l[j-1]
			j -= 1
		l[j] = aux


def bubbleSort(l: list, n: int) -> None:
	for i in range(n-1):
		for j in range(n-i-1):
			# compara
			if l[j] > l[j+1]:
				# troca
				# aux = l[j]
				# l[j] = l[j+1]
				# l[j+1] = aux
				l[j], l[j+1] = l[j+1], l[j]


def main():
	l = [7, 32, 3, 10, 22, 9]
	print(l)
	selectionSort(l, len(l))
	# insertionSort(l, len(l))
	# bubbleSort(l, len(l))
	print(l)
	
if __name__ == "__main__":
    main()
