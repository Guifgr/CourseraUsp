def dimensoes(x):
		X = "X"
		L = str(len(x))
		C = str(len(x[0]))
		resul = L+X+C
		print(resul)
		return resul

minha_matriz = [[1, 2, 3], [4, 5, 6]]

print(dimensoes(minha_matriz))