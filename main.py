import pygame, random
from pygame.locals import *

#   INICIANDO O PYGAME
pygame.init()

#   CONSTANTES
CIMA, BAIXO, DIREITA, ESQUERDA = 0, 1, 2, 3
LARGURA_TELA, ALTURA_TELA = 600,400
BRANCO, PRETO, VERMELHO, VERDE, AZUL, AMARELO = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)

# DECLARAÇÃO DAS SPRITES    
sprite_cabeca = {
    
    CIMA: pygame.image.load('Graphics/cabeca_cima.png'),
    BAIXO: pygame.image.load('Graphics/cabeca_baixo.png'),
    DIREITA: pygame.image.load('Graphics/cabeca_direita.png'),
    ESQUERDA: pygame.image.load('Graphics/cabeca_esquerda.png')
    
}

sprite_calda = {
    
    CIMA: pygame.image.load('Graphics/calda_cima.png'),
    BAIXO: pygame.image.load('Graphics/calda_baixo.png'),
    DIREITA: pygame.image.load('Graphics/calda_esquerda.png'),
    ESQUERDA: pygame.image.load('Graphics/calda_direita.png')
    
}

sprite_corpo = {
    
    'vertical': pygame.image.load('Graphics/corpo_vertical.png'),
    'horizontal': pygame.image.load('Graphics/corpo_horizontal.png'),
    'curva_baixo_esquerda': pygame.image.load('Graphics/corpo_baixo_esquerdo.png'),
    'curva_baixo_direita': pygame.image.load('Graphics/corpo_baixo_direito.png'),
    'curva_cima_direita': pygame.image.load('Graphics/corpo_cima_direito.png'),
    'curva_cima_esquerda': pygame.image.load('Graphics/corpo_cima_esquerdo.png')

}

sprite_maca = pygame.image.load('Graphics/maca.png')

#   CONFIRGURAÇÃO DA TELA
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Snake - Game")

#   FUNÇÕES AUXILIARES
def criar_surface_cor(tamanho, cor):
    surface = pygame.Surface(tamanho)
    surface.fill(cor)
    return surface

def desenhar_serpente(tela, serpente, direcaoSerpente):
    for i, pos in enumerate(serpente):
        if i == 0:  # Cabeça da serpente
            tela.blit(sprite_cabeca[direcaoSerpente], pos)
        elif i == len(serpente) - 1: #  Calda da serpente
            direcao_calda = obter_direcao_calda(serpente[i - 1], serpente[i])
            tela.blit(sprite_calda[direcao_calda], pos)
        else:
            direcao_anterior = obter_direcao(serpente[i - 1], serpente[i])
            direcao_proximo = obter_direcao(serpente[i], serpente[i + 1])
            sprite = obter_sprite_corpo(direcao_anterior, direcao_proximo)
            tela.blit(sprite, pos)
                      
def obter_direcao(pos_atual, pos_prox):
    x_atual, y_atual = pos_atual
    x_proximo, y_proximo = pos_prox
    
    if x_proximo > x_atual:
        return DIREITA
    elif x_proximo < x_atual:
        return ESQUERDA
    elif y_proximo > y_atual:
        return CIMA
    elif y_proximo < y_atual:
        return BAIXO

def obter_direcao_calda(pos_anterior, pos_calda):
    return obter_direcao(pos_calda, pos_anterior)

def obter_sprite_corpo(direcao_anterior, direcao_proximo):
    if direcao_anterior in (CIMA, BAIXO) and direcao_proximo in (CIMA, BAIXO):
        return sprite_corpo['vertical']
    elif direcao_anterior in (DIREITA, ESQUERDA) and direcao_proximo in (DIREITA, ESQUERDA):
        return sprite_corpo['horizontal']
    elif direcao_anterior == CIMA and direcao_proximo == DIREITA or direcao_anterior == ESQUERDA and direcao_proximo == BAIXO:
        return sprite_corpo['curva_cima_direita']
    elif direcao_anterior == CIMA and direcao_proximo == ESQUERDA or direcao_anterior == DIREITA and direcao_proximo == BAIXO:
        return sprite_corpo['curva_cima_esquerda']
    elif direcao_anterior == BAIXO and direcao_proximo == DIREITA or direcao_anterior == ESQUERDA and direcao_proximo == CIMA:
        return sprite_corpo['curva_baixo_direita']
    elif direcao_anterior == BAIXO and direcao_proximo == ESQUERDA or direcao_anterior == DIREITA and direcao_proximo == CIMA:
        return sprite_corpo['curva_baixo_esquerda']    

def desenha_linhas():
    # Desenha linhas horizontais
    for y in range(0, 400, 20):
        pygame.draw.line(tela, (50, 50, 50), (0, y), (LARGURA_TELA, y))  # Linha horizontal
    for x in range(0, 600, 20):
        pygame.draw.line(tela, (50, 50, 50), (x, 0), (x, ALTURA_TELA))  # Linha vertical
        
def desenha_mensagem (tela, tipoTexto, mensagem, cor, posicao):
    
    fontes = {
        "padrao": pygame.font.SysFont("arial", 30),
        "titulo": pygame.font.SysFont("arial", 40),
        "descricao": pygame.font.SysFont("arial", 25),
        "pontuacao": pygame.font.SysFont("arial", 20),
    }
    
    font = fontes.get(tipoTexto, fontes["padrao"])
    tela.blit(font.render(mensagem, True, cor), posicao)
    
def mostrar_pausa(pontuacao):
    tela.fill(PRETO)
    desenha_mensagem(tela, "titulo", "PAUSA", AMARELO, (200,10))
    desenha_mensagem(tela, "descricao", "Pressione qualquer tecla para retornar", AMARELO, (10,100))
    desenha_mensagem(tela, "pontuacao", f'Pontuacao atual: {pontuacao}', AMARELO, (10,50))
    pygame.display.update()

def checar_colisao_laterais(posicao):
    x, y = posicao
    if x < 0 or x >= LARGURA_TELA or y < 0 or y >= ALTURA_TELA:
        return True
    return False

def checar_colisao_maca(cabeca, maca):
    return cabeca == maca

def checar_colisao_corpo(serpente):
    cabeca = serpente[0]
    return cabeca in serpente[1:]

def gerar_posicao_aleatoria(serpente):
    while True:
        posicao = (random.randint(0, (LARGURA_TELA - 20) // 20) * 20,
                   random.randint(0, (ALTURA_TELA - 20) // 20) * 20)
        if posicao not in serpente:
            return posicao
        
def menuInicial():
    tela.fill((0, 0, 0))  # Limpa a tela    
    desenha_mensagem(tela, "titulo", "Snake-Game", AMARELO, (200,10))
    desenha_mensagem(tela, "padrao", "Selecione o modo de jogo:", AMARELO, (140,100))
    desenha_mensagem(tela, "descricao", "Normal (1)", VERDE, (160,130))
    desenha_mensagem(tela, "descricao", "Médio (2) ", AMARELO, (160,160))
    desenha_mensagem(tela, "descricao", "Dificil (3)", VERMELHO, (160,190))
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_1:
                    return 'facil'
                if event.key == K_2:
                    return 'medio'
                if event.key == K_3:
                    return 'dificil'
    
def fim_jogo_colisao(pontuacao, dificuldade):
    tela.fill(PRETO)
    desenha_mensagem(tela, "titulo", "Game-Over", AMARELO, (200, 10))
    desenha_mensagem(tela, "descricao", f'Pontuação total na dificuldade {dificuldade}: {pontuacao} ' , VERMELHO, (50, 100))
    desenha_mensagem(tela, "descricao", "Pressione qualquer tecla para retornar", VERMELHO, (50, 120))
    pygame.display.update()
    esperando_acao = True
    while esperando_acao:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                esperando_acao = False

def jogo(dificuldade):
    serpente = [(200, 200), (180, 200), (160, 200)]
    maca = gerar_posicao_aleatoria(serpente)
    direcaoSerpente, proximaDirecao = DIREITA, DIREITA
    pausado, pontos, velocidade = False,  0, 100
    
    if dificuldade == 'medio':
        incrementarVelocidade = 5
    elif dificuldade == 'dificil':
        incrementarVelocidade = 10
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
                
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pausado = not pausado
                elif pausado:
                    pausado = False
                elif event.key == K_LEFT or event.key == K_a:
                    if direcaoSerpente != DIREITA:
                        proximaDirecao = ESQUERDA
                elif event.key == K_RIGHT or event.key == K_d: 
                    if direcaoSerpente != ESQUERDA:
                        proximaDirecao = DIREITA
                elif event.key == K_UP or event.key == K_w:
                    if direcaoSerpente != BAIXO:
                        proximaDirecao = CIMA
                elif event.key == K_DOWN or event.key == K_s:
                    if direcaoSerpente != CIMA:
                        proximaDirecao = BAIXO
        
        if pausado:
            mostrar_pausa(pontos)
            continue

        # Atualiza a posição da serpente
        if proximaDirecao == ESQUERDA:
            nova_posicao = (serpente[0][0] - 20, serpente[0][1])
        elif proximaDirecao == DIREITA:
            nova_posicao = (serpente[0][0] + 20, serpente[0][1])
        elif proximaDirecao == CIMA:
            nova_posicao = (serpente[0][0], serpente[0][1] - 20)
        elif proximaDirecao == BAIXO:
            nova_posicao = (serpente[0][0], serpente[0][1] + 20)

        if checar_colisao_laterais(nova_posicao) or checar_colisao_corpo([nova_posicao] + serpente[:-1]):
            fim_jogo_colisao(pontos, dificuldade)
            return
        
        if checar_colisao_maca(nova_posicao, maca):
            serpente.append(serpente[-1])  # Aumenta o tamanho da serpente
            maca = gerar_posicao_aleatoria(serpente)  # Gera nova posição para a maçã
            pontos = pontos + 1
            
            if dificuldade == 'medio' and pontos % 10 == 0:
                velocidade = max(10, velocidade - incrementarVelocidade)
            if dificuldade == 'dificil'and velocidade > 60:
                velocidade = max(10, 100 - pontos)

        serpente = [nova_posicao] + serpente[:-1]
        direcaoSerpente = proximaDirecao

        tela.fill((55, 195, 55))  # Limpa a tela
        #desenha_linhas()
        desenhar_serpente(tela, serpente, direcaoSerpente)
        tela.blit(sprite_maca, maca)
        desenha_mensagem(tela, "pontuacao", f'Pontuacao: {pontos}', AMARELO, (10,10))
        desenha_mensagem(tela, "pontuacao", f'Velocidade: {velocidade}', AMARELO, (10,30))
        pygame.display.update()
        pygame.time.delay(velocidade)  # Delay para controlar a velocidade da serpente

while(True):
    dificuldade = menuInicial()
    jogo(dificuldade)