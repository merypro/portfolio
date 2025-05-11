
# Coin Catcher - Simple Arcade Game
# Author: Mahri Akmuradova

import pygame
import random

pygame.init()
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coin Catcher")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 223, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()
FPS = 60

player_size = 60
player = pygame.Rect(WIDTH//2 - player_size//2, HEIGHT - 80, player_size, player_size)
player_speed = 7

item_width, item_height = 40, 40
coin_speed = 4
bomb_speed = 6
coins = []
bombs = []

score = 0
font = pygame.font.SysFont(None, 36)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

def spawn_coin():
    x = random.randint(0, WIDTH - item_width)
    coins.append(pygame.Rect(x, -item_height, item_width, item_height))

def spawn_bomb():
    x = random.randint(0, WIDTH - item_width)
    bombs.append(pygame.Rect(x, -item_height, item_width, item_height))

running = True
spawn_timer = 0

while running:
    clock.tick(FPS)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed

    spawn_timer += 1
    if spawn_timer % 40 == 0:
        spawn_coin()
    if spawn_timer % 90 == 0:
        spawn_bomb()

    for coin in coins[:]:
        coin.y += coin_speed
        if coin.top > HEIGHT:
            coins.remove(coin)
        elif player.colliderect(coin):
            score += 1
            coins.remove(coin)

    for bomb in bombs[:]:
        bomb.y += bomb_speed
        if bomb.top > HEIGHT:
            bombs.remove(bomb)
        elif player.colliderect(bomb):
            running = False

    pygame.draw.rect(screen, BLUE, player)
    for coin in coins:
        pygame.draw.ellipse(screen, YELLOW, coin)
    for bomb in bombs:
        pygame.draw.ellipse(screen, RED, bomb)

    draw_text(f"Score: {score}", font, BLACK, screen, 10, 10)
    pygame.display.flip()

pygame.quit()
