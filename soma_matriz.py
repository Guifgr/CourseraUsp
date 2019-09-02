def soma_matrizes(x,y):
		resul = x
		if len(x) == len(y) and len(x[0]) == len(y[0]):
				for i in range(len(x)):
						for j in range(len(x[1])):
								resul[i][j] = x[i][j] + y[i][j]
		else:
				resul = False
		return resul 
