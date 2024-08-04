import pygame
import random
from random import randint
from pygame.locals import *

#   CONSTANTES
CIMA, BAIXO, DIREITA, ESQUERDA = 0, 1, 2, 3

# INICIANDO PYGAME
pygame.init()
fontePontos = pygame.font.SysFont("arial", 20)
fonteFimJogo = pygame.font.SysFont("arial", 40)

# FUNÇÕES

#   GERANDO POSIÇÕES ALEATORIAS PARA A MAÇÃ
#   380 PARA EIXO X E 380 PARA EIXO Y POIS COMO A MAÇA E A Serpente VÃO OCUPAR 20 QUADRADINHOS,
#   E A MATRIZ COMEÇA A SER CONTADA DO LADO SUPERIOR ESQUERDO, ELAS PODERIAM SUMIR AO SEREM GERADAS NO LIMITE DA TELA
def posicaoAleatoria():
    x = (random.randint(0, 380))
    y = (random.randint(0, 380))
    return (x//20)*20, (y//20)*20


# VERIFICANDO SE AS COORDENADAS DO EIXO X E Y DA Serpente SÃO AS MESMAS DA MAÇA
def colisao(serp, mac):
    return (serp[0] == mac[0]) and (serp[1] == mac[1])


def fimDeJogo(pontuacaoFinal):
    mensagemFimJogo = fonteFimJogo.render(
        "Fim De Jogo!", True, (255, 255, 0))
    ultimaPontuacao = fontePontos.render(
        f'Pontuação Total: {pontuacaoFinal}', True, (255, 255, 0))
    tela.blit(mensagemFimJogo, [80, 140])
    tela.blit(ultimaPontuacao, [120, 190])
    pygame.display.update()
    pygame.time.wait(5000)
    pygame.quit()
    exit()

    #   CRIAMOS A TELA COM UMA MATRIZ 400x400, E ATRIBUIMOS O TITULO DE JOGO DA SERPENTE A JANELA


tela = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Jogo Da Serpente')

#   CRIAMOS A Serpente COMO UMA LISTA DE TUPLAS, DEFINIMOS O TAMANHO DO QUADRADO DA Serpente, QUE SERA 20x20
#   ATRIBUIMOS A COR VERDE A Serpente COM O SISTEMA RGB E ATRIBUIMOS A DIREÇÃO INICIAL QUE A Serpente TOMARA

Serpente = [(200, 200), (220, 200), (240, 200)]
peleSerpente = pygame.Surface((20, 20))
peleSerpente.fill((0, 255, 0))
direcaoSerpente = DIREITA

#   CRIAMOS A MAÇA COM A POSICÃO INICIAL NA COORDENADA 360,200 ATRIBUIMOS O TAMANHO DO SEU QUADRADO QUE SERA 20x20
#   E A PINTAMOS DE VERMELHA USANDO O SISTEMA RGB

posicaoMaca = (360, 200)
maca = pygame.Surface((20, 20))
maca.fill((255, 0, 0))

#   CRIAMOS UM DELIMITADOR DE FPS PARA O JOGO E INICIAMOS A VARIAVEL QUE RECEBERA A PONTUAÇÃO DO USUARIO
fps = pygame.time.Clock()
pontos = 0

while True:

    pontuacao = fontePontos.render(f'Pontuação: {pontos}', True, (255, 255, 0))
    fps.tick(7)
    tela.fill((0, 0, 0))

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            exit()

        #   PROCURANDO EVENTOS DO TECLADO
        if event.type == KEYDOWN:

            if event.key == K_w and direcaoSerpente != BAIXO:
                direcaoSerpente = CIMA

            if event.key == K_s and direcaoSerpente != CIMA:
                direcaoSerpente = BAIXO

            if event.key == K_a and direcaoSerpente != DIREITA:
                direcaoSerpente = ESQUERDA

            if event.key == K_d and direcaoSerpente != ESQUERDA:
                direcaoSerpente = DIREITA

    #   CHAMANDO A FUNÇÃO QUE VERIFICA SE A Serpente COLIDIU COM A MAÇÃ
    if colisao(Serpente[0], posicaoMaca):
        posicaoMaca = posicaoAleatoria()
        Serpente.append((0, 0))
        pontos += 1

    #   VERIFICA SE A MAÇA NASCEU ONDE A Serpente ESTÁ
    while posicaoMaca in Serpente:
        posicaoMaca = posicaoAleatoria()

    #   VERIFICANDO SE A Serpente COLIDIU COM O LIMITE DA TELA
    if Serpente[0][0] == 400 or Serpente[0][1] == 400 or Serpente[0][0] < 0 or Serpente[0][1] < 0:
        fimDeJogo(pontos)

    #   VERIFICA SE A Serpente COLIDIU/SOBREPOS SUA COORDENADA
    for contador in range(1, len(Serpente) - 1):
        if Serpente[0][0] == Serpente[contador][0] and Serpente[0][1] == Serpente[contador][1]:
            fimDeJogo(pontos)

    #   DÁ O SENTIDO DE MOVIMENTO DÁ Serpente
    for i in range(len(Serpente) - 1, 0, -1):
        Serpente[i] = (Serpente[i-1][0], Serpente[i-1][1])

    #   SE A Serpente ESTÁ INDO PARA CIMA, O EIXO Y DELA ESTÁ DECRESCENDO
    if direcaoSerpente == CIMA:
        Serpente[0] = (Serpente[0][0], Serpente[0][1] - 20)

    #   SE A Serpente ESTÁ INDO PARA CIMA, O EIXO Y DELA ESTÁ DECRESCENDO
    if direcaoSerpente == BAIXO:
        Serpente[0] = (Serpente[0][0], Serpente[0][1] + 20)

    #   SE A Serpente ESTÁ INDO PARA DIREITA, O EIXO X DELA ESTÁ CESCENDO
    if direcaoSerpente == DIREITA:
        Serpente[0] = (Serpente[0][0] + 20, Serpente[0][1])

    #   SE A Serpente ESTÁ INDO PARA ESQUEDA, O EIXO X DELA ESTÁ DECRESCENDO
    if direcaoSerpente == ESQUERDA:
        Serpente[0] = (Serpente[0][0] - 20, Serpente[0][1])

    #   MOSTRANDO A MAÇA NA TELA
    tela.blit(maca, posicaoMaca)

    #   MOSTRANDO TODA A Serpente
    for pos in Serpente:
        tela.blit(peleSerpente, pos)

    #   ATUALIZANDO A TELA
    tela.blit(pontuacao, [0, 0])
    pygame.display.update()
