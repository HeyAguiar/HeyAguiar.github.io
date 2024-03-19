import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definições de tela
WIDTH, HEIGHT = 600, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Definições do jogador
PLAYER_WIDTH, PLAYER_HEIGHT = 10, 60
PLAYER_SPEED = 5
player = pygame.Rect(50, HEIGHT // 2 - PLAYER_HEIGHT // 2, PLAYER_WIDTH, PLAYER_HEIGHT)

# Definições do computador
computer = pygame.Rect(WIDTH - 50 - PLAYER_WIDTH, HEIGHT // 2 - PLAYER_HEIGHT // 2, PLAYER_WIDTH, PLAYER_HEIGHT)

# Bola
BALL_WIDTH, BALL_HEIGHT = 10, 10
ball = pygame.Rect(WIDTH // 2 - BALL_WIDTH // 2, HEIGHT // 2 - BALL_HEIGHT // 2, BALL_WIDTH, BALL_HEIGHT)
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))

# Loop principal do jogo
clock = pygame.time.Clock()
running = True
while running:
    # Manipulação de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimento do jogador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= PLAYER_SPEED
    if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.y += PLAYER_SPEED

    # Movimento da bola
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Colisão da bola com as paredes
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x *= -1

    # Colisão da bola com os jogadores
    if ball.colliderect(player) or ball.colliderect(computer):
        ball_speed_x *= -1

    # Desenhar objetos na tela
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, WHITE, player)
    pygame.draw.rect(WIN, WHITE, computer)
    pygame.draw.ellipse(WIN, WHITE, ball)
    pygame.draw.aaline(WIN, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Atualizar a tela
    pygame.display.update()
    clock.tick(60)

# Encerrar o Pygame
pygame.quit()
