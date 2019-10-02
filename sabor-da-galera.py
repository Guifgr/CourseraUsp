correto = False

while correto == False:
    pessoas = int(input('Quantas pessoas vão comer?\n'))
    correto = input("Você digitou: "+str(pessoas)+" pessoas está correto?\n")
    correto = correto.lower()
    if correto == 's' or correto == 'sim' or correto == 'y' or correto == 'yes':
        correto = True
    else:
        correto = False

correto = False

while correto == False:
    sabores = int(input('Quantos sabores tem?\n'))
    correto = input("Você digitou: "+str(sabores)+" sabores está correto?\n")
    correto = correto.lower()
    if correto == 's' or correto == 'sim' or correto == 'y' or correto == 'yes':
        correto = True
    else:
        correto = False
correto = False

flavor = [''] * sabores
tempflavor = [0]*sabores
final = tempflavor[:]
while correto == False:
    for i in range(sabores):
        flavor[i] = input("Qual o sabor numero: "+str(i+1)+"?: ")

    print("\n\nOs sabores são:")

    for i in range(sabores):
        print(str(flavor[i])+"")

    print("\n")
    
    correto = input("Estão corretos?\n")
    if correto == 's' or correto == 'sim' or correto == 'y' or correto == 'yes':
        correto = True
    else:
        correto = False
correto = False

print('\n\n\n\n\nAgora vamos ver os sabores de cada um!')
for j in range(pessoas):
    #^aqui vamos rodar pessoas
    for i in range(sabores):
        #^aqui vamos rodar cada sabor
        tempflavor[i] = int(input("Pessoa n°["+str(j+1)+"] do sabor "+flavor[i]+" vai querer quantas?: "))
        while correto == False:
            #^aqui é a verificacao de cada sabor
            correto = input("Digitou corretamente?\n")
            if correto == 's' or correto == 'sim' or correto == 'y' or correto == 'yes':
                correto = True
                final[i] += tempflavor[i]
            else:
                correto = False    
        correto = False    
                
    for k in range(sabores):
        print("\nVocê escolheu "+str(tempflavor[k])+"  do sabor "+ flavor[k])  
    print("\n")

for l in range(sabores):
    print("Do sabor "+flavor[l]+" no total são: "+str(final[l]))

    
