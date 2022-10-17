import random
from tkinter import *
from tkinter import ttk

# main_win = Tk()

# frame = ttk.Frame(main_win, padding=10)
# frame.grid()
# ttk.Label(frame, text="Hello World!").grid(column=0, row=0)
# numero_jogadores = ttk.Entry(frame, textvariable="Digite o número de jogadores").grid(column=1,row=0)
# ttk.Button(frame, text="Quit", command=main_win.destroy).grid(column=0, row=1)
# main_win.mainloop()


def criar_baralho():
    naipes = ['♥','♦','♣','♠']

    baralho = []

    for naipe in naipes:

        for i in range(1, 14):

            if (i == 1):
                carta = [naipe, 'Ás', 1]
            elif (i == 11):
                carta = [naipe, 'Valete', 10]
            elif (i == 12):
                carta = [naipe, 'Dama', 10]
            elif (i == 13):
                carta = [naipe, 'Rei', 10]
            else:
                carta = [naipe, str(i), i]

            baralho.append(carta)

    return baralho


def sorteio(baralho):
    carta = baralho.pop(random.randint(0, len(baralho)-1))
    print(f'A carta sorteada foi {carta[1]} de {carta[0]} que vale {carta[2]} pontos.')
    print(f'Restam {len(baralho)} cartas no baralho.')
    return carta


def jogada(jogador, baralho, mesa=False):

    if mesa == True:
        resposta = 'S'
    else:
        resposta = ''

    while(resposta != 'N' and resposta != 'S'):
        resposta = input(f'{jogador[0]}, deseja comprar uma carta (S/N): ').upper()

    if resposta.upper() == 'S':
        carta = sorteio(baralho)

        jogador[2] += int(carta[2])

        # jogador[1] = not jogador[2] > 21
        if jogador[2] >= 21:
            jogador[1] = False
            print(f'O jogador {jogador[0]} superou 21 pontou e não pode mais fazer jogadas!')
        else:
            print(f'Pontuação atual do jogador {jogador[0]}: {jogador[2]} pontos.')
    else:
        print(f'O jogador {jogador[0]} escolheu parar. A pontuação atual foi de {jogador[2]} pontos!')
        jogador[1] = False


def pontuacao(jogadores):
    maior_pontuacao = []
    maior_jogador = []

    for jogador in jogadores:

        if jogador[2] <= 21:
            maior_pontuacao.append(jogador[2])
            maior_jogador.append(jogador[0])

    pontuacao_maxima = max(maior_pontuacao)
    for i in range(len(maior_pontuacao)):
        if(maior_pontuacao[i] == pontuacao_maxima):
            if(maior_jogador[i] == 'Mesa'):
                print('A mesa fez mais pontos. Portanto, ninguém ganhou!')
            else:
                print(f'O jogador {maior_jogador[i]} teve a maior pontuação: {maior_pontuacao[i]} pontos')
    


def blackjack():
    numero_jogadores = int(input('Digite o número de jogadores: '))

    jogadores = []

    for i in range(numero_jogadores):
        while not nome:
            nome = input('Digite o nome do jogador: ')
        jogador = [nome, True, int(0)]
        jogadores.append(jogador)

    jogadores.append(['Mesa', True, int(0)])
    
    baralho = criar_baralho()
    jogo_ativo = True

    i=0
    while jogo_ativo:
        if(jogadores[i][1]):
            jogada(jogadores[i], baralho, jogadores[i][0]=='Mesa')
            #print(f'Pontuação atual do jogador {jogadores[i][0]}: {jogadores[i][2]} pontos.')
        i += 1

        if(i == len(jogadores)):
            i = 0
        
        for jogador in jogadores[:-1]:
            if(jogador[1]) == True:
                break
        else:
            jogo_ativo = False
    
    pontuacao(jogadores)

    print('Fim de jogo')



blackjack()