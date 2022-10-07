import pygame  # IMPORTAMOS O PYGAME
import random
from pygame.locals import *


def on_grid_random():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return (x//10 * 10, y//10 * 10)


def colisao(c1, c2):
    return (c1[0] == c2[0] and c1[1] == c2[1])


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption(('Snake'))

snake = [(200, 200), (210, 200), (220, 200)]
snake_body = pygame.Surface((10, 10))
snake_body.fill((255, 255, 255))
sk_direcao = LEFT

maca_pos = on_grid_random()
maca = pygame.Surface((10, 10))
maca.fill((255, 0, 0))

Velocidade = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 18)
score = 0

game_over = False
while not game_over:
    Velocidade.tick(15)
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP and sk_direcao != DOWN:
                sk_direcao = UP
            if event.key == K_DOWN and sk_direcao != UP:
                sk_direcao = DOWN
            if event.key == K_LEFT and sk_direcao != RIGHT:
                sk_direcao = LEFT
            if event.key == K_RIGHT and sk_direcao != LEFT:
                sk_direcao = RIGHT

    if colisao(snake[0], maca_pos):
        maca_pos = on_grid_random()
        snake.append((0, 0))
        score = score + 1

    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
        game_over = True
        break

    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True
            break

    if game_over:
        break

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if sk_direcao == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)

    if sk_direcao == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)

    if sk_direcao == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])

    if sk_direcao == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    screen.fill((0, 0, 0))
    screen.blit(maca, maca_pos)

    for x in range(0, 600, 10):
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 600))

    for y in range(0, 600, 10):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (600, y))

    score_font = font.render('Pontos: %s' % (score), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (600-120, 10)
    screen.blit(score_font, score_rect)

    for pos in snake:
        screen.blit(snake_body, pos)

    pygame.display.update()

while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 75)
    game_over_screen = game_over_font.render(
        'Fim De Jogo', True, (255, 255, 255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (600/2, 10)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
