x = input("Digite um número inteiro:")
limite = len(x)
soma = 0
while limite != 0:
		soma += int(x[limite-1])
		limite -= 1
else:
		print(soma)