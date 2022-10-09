##### 10 - Game over ####
import pygame
import random
from random import randint
from pygame.locals import *

# MACRO
CIMA = 0
DIREITA = 1
BAIXO = 2
ESQUERDA = 3

# INICIANDO PYGAME
pygame.init()

# FUNÇÕES


def posicaoAleatoria():
    x = (random.randint(0, 59)*10)
    y = (random.randint(0, 59)*10)
    return (x//20)*20, (y//20)*20


def colisao(cr, mc):
    return (cr[0] == mc[0]) and (cr[1] == mc[1])


def novasPosicoes():
    global cobra, peleCobra, diretacaoCobra, posicaoMaca, pontos, contador
    cobra = [(200, 200), (220, 200), (240, 200)]
    peleCobra = pygame.Surface((20, 20))
    peleCobra.fill((0, 255, 0))
    diretacaoCobra = DIREITA
    posicaoMaca = posicaoAleatoria()
    pontos = 0
    contador = 220


def menuFimJogo(valorColidiu):

    if valorColidiu == True:
        while valorColidiu:
            quadGameOver.midtop = (760 / 2, 10)
            tela.blit(telaGameOver, quadGameOver)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    valorColidiu = False
                    exit()

                if event.type == KEYDOWN:
                    if event.key == K_r:
                        novasPosicoes()
                        valorColidiu = False


# SONS
pygame.mixer.music.set_volume(0.05)
musicaFundo = pygame.mixer.music.load('sons/BoxCat_Games_Tricks.mp3')
pygame.mixer.music.play(-1)
somColisao = pygame.mixer.Sound('sons/smw_stomp.wav')
somColisao.set_volume(0.1)

tela = pygame.display.set_mode((760, 760))
pygame.display.set_caption('Cobrinha')

cobra = [(200, 200), (220, 200), (240, 200)]
peleCobra = pygame.Surface((20, 20))
peleCobra.fill((0, 255, 0))
diretacaoCobra = DIREITA

posicaoMaca = posicaoAleatoria()
maca = pygame.Surface((20, 20))
maca.fill((255, 0, 0))

tempo = pygame.time.Clock()
fonte = pygame.font.SysFont('arial', 40, True, True)
pontos = 0

fonteGameOver = pygame.font.Font('freesansbold.ttf', 75)
telaGameOver = fonteGameOver.render('Fim de jogo', True, (0, 0, 0))
quadGameOver = telaGameOver.get_rect()
contador = 0

gameOver = False
while not gameOver:

    tempo.tick(15)
    formataPonto = f'Pontuação: {pontos}'
    pontuacao = fonte.render(formataPonto, True, (0, 0, 0))
    tela.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            gameOver = True
            exit()

        if event.type == KEYDOWN:

            if event.key == K_w and diretacaoCobra != BAIXO:
                diretacaoCobra = CIMA

            if event.key == K_s and diretacaoCobra != CIMA:
                diretacaoCobra = BAIXO

            if event.key == K_a and diretacaoCobra != DIREITA:
                diretacaoCobra = ESQUERDA

            if event.key == K_d and diretacaoCobra != ESQUERDA:
                diretacaoCobra = DIREITA

    if colisao(cobra[0], posicaoMaca):
        posicaoMaca = posicaoAleatoria()
        cobra.append((0, 0))
        somColisao.play()
        pontos += 1

    if cobra[0][0] == 760 or cobra[0][1] == 760 or cobra[0][0] < 0 or cobra[0][1] < 0:
        menuFimJogo(True)

    for contador in range(1, len(cobra) - 1):
        if cobra[0][0] == cobra[contador][0] and cobra[0][1] == cobra[contador][1]:
            menuFimJogo(True)

    for i in range(len(cobra) - 1, 0, -1):
        cobra[i] = (cobra[i-1][0], cobra[i-1][1])

    if diretacaoCobra == CIMA:
        cobra[0] = (cobra[0][0], cobra[0][1] - 20)

    if diretacaoCobra == BAIXO:
        cobra[0] = (cobra[0][0], cobra[0][1] + 20)

    if diretacaoCobra == DIREITA:
        cobra[0] = (cobra[0][0] + 20, cobra[0][1])

    if diretacaoCobra == ESQUERDA:
        cobra[0] = (cobra[0][0] - 20, cobra[0][1])

    tela.blit(maca, posicaoMaca)

    for pos in cobra:
        tela.blit(peleCobra, pos)

    tela.blit(pontuacao, (420, 40))
    pygame.display.update()
