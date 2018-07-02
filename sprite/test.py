# -*- coding:utf-8 -*-

import pygame, sys, random
from pygame.locals import *
from sprite import MySprite

def print_text(font, x, y, text, color=(255, 255, 255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))

def reset_flame(f):
    y = random.randint(350, 350+40)
    f.position = 600, y

pygame.init()
screen = pygame.display.set_mode((600, 480), 0, 32)
pygame.display.set_caption("Sprite Animateion Demo")
font = pygame.font.Font(None, 18)
framerate = pygame.time.Clock()

group = pygame.sprite.Group()

role = MySprite(screen)
role.load("Images/bone_walk.png", 64, 64, 9)
role.position = (300, 350)
group.add(role)

flame = MySprite(screen)
flame.load("Images/flame.png", 28, 13, 1)
flame.position = (600, 350)
group.add(flame)

dragon = MySprite(screen)
dragon.load("Images/dragon.png", 176, 176, 16)
dragon.position = (-50, 280)
group.add(dragon)

flame_vel = 10
game_over = False
player_start_y = role.Y
player_jumping = False
jump_vel = 0.0

while True:
    framerate.tick(13)
    ticks = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        sys.exit()
    elif key[pygame.K_SPACE]:
        if not player_jumping:
            player_jumping = True
            jump_vel = -25.0

    if not game_over:
        flame.X -= flame_vel
        if flame.X < -40:
            reset_flame(flame)

    if pygame.sprite.collide_rect_ratio(0.5)(flame, role):
        role.X -= 10
        reset_flame(flame)

    if pygame.sprite.collide_rect_ratio(0.5)(flame, dragon):
        dragon.X -= 10
        reset_flame(flame)

    if dragon.X < -150:
        print_text(font, 300, 150, "YOU WIN")

    if player_jumping:
        role.Y += jump_vel
        jump_vel += 5.0
        if role.Y > player_start_y:
            player_jumping = False
            role.Y = player_start_y
            jump_vel = 0.0
    
    pygame.draw.line(screen, pygame.Color(255, 255, 255, 0), (0, 350+63), (600, 350+63),5)
    group.update(ticks)
    group.draw(screen)
    sprite_str = str(role).split('-')
    i = 0
    for line in sprite_str:
        print_text(font, 0, i, line)
        i += 20
    print_text(font, 0, 460, "position:(%d, %d)" % role.position)
    pygame.display.update()
    screen.fill((40, 40, 40))