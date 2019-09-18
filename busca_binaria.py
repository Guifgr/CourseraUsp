def busca(lista, procurado):
    menor, fim = 0, len(lista) - 1
    while menor <= fim:
        meio = (menor + fim) // 2
        print(meio)
        if lista[meio] < procurado:
            menor = meio + 1
        elif procurado < lista[meio]:
            fim = meio - 1
        else:
            return meio
    return False