x = int(input("Digite o valor de n:"))
contador = x
numeros = 0
while contador != 0:
		if (numeros%2) != 0:
				print(numeros)
				contador -= 1
				numeros += 1
		else:
				numeros += 1