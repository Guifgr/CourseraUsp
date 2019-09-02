def maiusculas(frase):
		fraseM = frase.upper()
		resul = ''
		for i in range(len(fraseM)):
				if fraseM[i] == frase[i] and frase[i].isalpha() == True:
						resul += frase[i]
		resul = resul.replace(' ','')
		return resul