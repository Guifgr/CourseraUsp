def maximo(a,b,c):
		if a <= b:
				aux = b
				a = aux
				b = a
				if a <= c:
						return c
				else:
						return a