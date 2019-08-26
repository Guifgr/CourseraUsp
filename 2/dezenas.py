valor = input("Digite um número inteiro:")
tamanho = len(valor);
posicao = tamanho-2;
tamanho = str(tamanho);
if(tamanho < "2"):
    print("O dígito das dezenas é 0")
else:
    dezena = valor[posicao];
    print("O dígito das dezenas é",dezena)