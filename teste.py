import pygame
from pygame.locals import *

'''
INICIANDO A TELA DO PYGAME
DEFININDO O TAMANHO DA TELA LARGURA(650) ALTURA(500)
DEFININDO O TITULO DA JANELA
'''
pygame.init()
largura = 650
altura = 650
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('JOGO')

# LOOP PRINCIPAL DO JOGO
while True:

    # CHECAR OS EVENTOS
    for event in pygame.event.get():

        # FECHA A JANELA
        if event.type == QUIT:
            pygame.quit()
            exit()

    '''
    DESENHA UM RETANDGULO NA TELA
    cor_ret DEFINE A COR DO RETANGULO, SEGUINDO O SISTEMA RGB
    pos_ret DEFINE A POSIÇÃO DO RETANGULO SEGUINDO COORDENADAS
    '''
    cor_ret,  pos_ret = (255, 0, 0), (10, 250, 40, 30)
    pygame.draw.rect(tela, cor_ret, pos_ret)

    '''
    DESENHA UM CIRCULO NA TELA
    cor_cor DEFINE A COR DO CIRCULO
    pos_cir DEFINE A POSIÇÃO DO CIRCULO
    rad_cir  DEFINE O RADIO DO CIRCULO
    '''
    cor_cir, pos_cir, rad_cir = (255, 255, 0), (50, 150), 30
    pygame.draw.circle(tela, cor_cir, pos_cir, rad_cir)

    '''
     DESENHA UMA LINHA NA TELA
    cor_lin DEFINE A COR DA LINHA
    pos_ini DEFINE A POSIÇÃO INICIAL
    pos_fin DEFINE A POSIÇÃO FINAL
    esp_lin DEFINE A ESPESSURA DA LINHA
    '''
    cor_lin, pos_ini, pos_fin, esp_lin = (
        255, 255, 2550), (390, 0), (390, 650), 5
    pygame.draw.line(tela, (255, 255, 255), (390, 0), (390, 650), 5)

    # ATUALIZA A TELA DO JOGO A CADA LOOP
    pygame.display.update()
