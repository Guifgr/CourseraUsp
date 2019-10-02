def pessoas():
    correto = False

    while correto == False:
        pessoas = int(input('Quantas pessoas vão comer?\n'))
        correto = input("Você digitou: "+str(pessoas)+" pessoas está correto?\n")
        correto = correto.lower()
        if correto == 's' or correto == 'sim' or correto == 'y' or correto == 'yes':
            correto = True
        else:
            correto = False
        return pessoas

def sabores():
    correto = False        
    while correto == False:
        sabores = int(input('Quantos sabores tem?\n'))
        correto = input("Você digitou: "+str(sabores)+" sabores está correto?\n")
        correto = correto.lower()
        if correto == 's' or correto == 'sim' or correto == 'y' or correto == 'yes':
            correto = True
        else:
            correto = False
    return sabores

def nomeSabores(comidas):
    flavor = [0] * comidas
    correto = False      

    while correto == False:
        for i in range(comidas):
            flavor[i] = input("Qual o sabor numero: "+str(i+1)+"?: ")

        print("\n\nOs sabores são:")

        for i in range(comidas):
            print(str(flavor[i])+"")

        print("\n")
        
        correto = input("Estão corretos?\n")
        if correto == 's' or correto == 'sim' or correto == 'y' or correto == 'yes':
            correto = True
        else:
            correto = False
    return flavor

def escolhas(pessoal,comidas,nomeDaComida,counter):
    correto = False 
    escolhas = [0] * comidas
    temp = escolhas
    
    for i in range(comidas):

        temp[i] = int(input("Pessoa n°["+str(counter+1)+"] do sabor "+nomeDaComida[i]+" vai querer quantas?: "))
        while correto == False:

            correto = input("Digitou corretamente?\n")
            if correto == 's' or correto == 'sim' or correto == 'y' or correto == 'yes':
                correto = True
                escolhas[i] += temp[i]
            else:
                correto = False    
        correto = False 
    return escolhas

def main():
    pessoal = pessoas()
    comidas = sabores()
    nomeDaComida = nomeSabores(comidas)

    print('\n\n\n\n\nAgora vamos ver os sabores de cada um!')
    
    final =[0]*comidas 
    for counter in range(pessoal):
        passaDados = escolhas(pessoal,comidas,nomeDaComida,counter)
        for i in range(comidas):
            final[i] += passaDados[i]
        

    for j in range(comidas):
        print("Do sabor "+nomeDaComida[j]+" no total são: "+str(final[j]))

if __name__ == "__main__":
    main()