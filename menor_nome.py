def menor_nome(nomes):
		menor = nomes[1]
		for i in range(len(nomes)):	
				nomes[i] = nomes[i].strip()
				nomes[i] = nomes[i].lower()
				if len(nomes[i]) < len(menor):
						menor = nomes[i]
		menor = menor.capitalize()
		return menor

print(menor_nome(['maria', 'josé', 'PAULO', 'Catarina']))	