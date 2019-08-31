def computador_escolhe_jogada(n, m):
    computador = 1
    while computador != m:
        if (n - computador) % (m+1) == 0:
            return computador
        else:
            computador += 1
    return computador
def usuario_escolhe_jogada(n, m):
    jogadorComeca = False
    while not jogadorComeca:
        jogador = int(input('Quantas peças você vai tirar? '))
        if jogador > m or jogador < 1:
            print()
            print('Oops! Jogada inválida! Tente de novo.')
            print()
        else:
            jogadorComeca = True
    return jogador
def campeonato():
    rounds = 1
    while rounds <= 3:
        print()
        print('**** Rodada', rounds, '****')
        print()
        partida()
        rounds += 1
    print()
    print('Placar: Você 0 X 3 Computador')
def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    computadorVez = False
    if n % (m+1) == 0:
        print()
        print('Voce começa!')
    else:
        print()
        print('Computador começa!')
        computadorVez = True
    while n > 0:
        if computadorVez:
            computador = computador_escolhe_jogada(n, m)
            n = n - computador
            if computador == 1:
                print()
                print('O computador tirou uma peça')
            else:
                print()
                print('O computador tirou', computador, 'peças')
            computadorVez = False
        else:
            jogador = usuario_escolhe_jogada(n, m)
            n = n - jogador
            if jogador == 1:
                print()
                print('Você tirou uma peça')
            else:
                print()
                print('Você tirou', jogador, 'peças')
            computadorVez = True
        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
            print()
        else:
            if n != 0:
                print('Agora restam,', n, 'peças no tabuleiro.')
                print()
    print('Fim do jogo! O computador ganhou!')
print('Bem-vindo ao jogo do NIM! Escolha:')
print()
print('1 - para jogar uma partida isolada')
campOrNot = int(input('2 - para jogar um campeonato '))
if campOrNot == 2:
    print()
    print('Voce escolheu um campeonato!')
    print()
    campeonato()
else:
    if campOrNot == 1:
        print()
        partida()