def ordenada(lista):
    for i in range(len(lista)-1):
        minIndex = i
        for j in range(i+1,len(lista)):
            if lista[j] < lista[minIndex]:
                minIndex = j
        if minIndex != i:
            return False
    return True