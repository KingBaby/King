# -*- coding:utf-8 -*-

import pygame, sys, random
from pygame.locals import *
from sprite import *

dragon_direction = Direction(1, 0, 4, 7)
player_direction = Direction(0, 3, 2, 1)
screen_width, screen_height = 900, 800
dragon_num = 10
player_moving = False
player_health = 100

def calc_velocity(direction, all_direction, vel = 1.0):
    velocity = Point(0, 0)
    if direction == all_direction.north:
        velocity.y = -vel
    elif direction == all_direction.east:
        velocity.x = vel
    elif direction == all_direction.south:
        velocity.y = vel
    elif direction == all_direction.west:
        velocity.x = -vel

    return velocity

def reverse_direction(sprite, all_direction):
    if sprite.direction == all_direction.north:
        sprite.direction = all_direction.south
    elif sprite.direction == all_direction.east:
        sprite.direction = all_direction.west
    elif sprite.direction == all_direction.south:
        sprite.direction = all_direction.north
    elif sprite.direction == all_direction.west:
        sprite.direction = all_direction.east


pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
pygame.display.set_caption("Zombie Mod Demo")
framerate = pygame.time.Clock()

dragon_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

player = MySprite()
player.load("Images/BODY_male64_64.png", 64, 64, 9)
player.position = screen_width - 128, screen_height - 128
player.direction = player_direction.south
player_group.add(player)


for n in range(0, dragon_num):
    dragon = MySprite()
    dragon.load("Images/dragon176_176.png", 176, 176, 16)
    dragon.position = random.randint(0, screen_width-176), random.randint(0, screen_height-176)
    dragon.direction = random.choice([dragon_direction.north, dragon_direction.east, dragon_direction.south, dragon_direction.west])
    dragon_group.add(dragon)

while True:
    framerate.tick(13)
    ticks = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        sys.exit()
    elif key[pygame.K_w]:
        player.direction = player_direction.north
        player_moving  = True
    elif key[pygame.K_s]:
        player.direction = player_direction.south
        player_moving = True
    elif key[pygame.K_a]:
        player.direction = player_direction.west
        player_moving = True
    elif key[pygame.K_d]:
        player.direction = player_direction.east
        player_moving = True
    else:
        player_moving = False

    player.first_frame = player.direction * player.columns
    player.last_frame = player.first_frame + player.columns - 1
    if player.frame < player.first_frame:
        player.frame = player.first_frame

    if not player_moving:
        player.frame = player.last_frame = player.first_frame
    else:
        player.velocity = calc_velocity(player.direction, player_direction, 8)
        player.velocity.x *= 1.5
        player.velocity.y *= 1.5

    if player_moving:
        player.X += player.velocity.x
        player.Y += player.velocity.y
        if player.X < 0:
            player.X  = 0
        elif player.X > screen_width - player.frame_width:
            player.X = screen_width - player.frame_width
        if player.Y < 0:
            player.Y = 0
        elif player.Y > screen_height - player.frame_height:
            player.Y = screen_height - player.frame_height
    player_group.update(ticks, 50)

    dragon_group.update(ticks, 50)
    for d in dragon_group:
        d.first_frame = d.direction * d.columns
        d.last_frame = d.first_frame + d.columns - 1
        if d.frame < d.first_frame:
            d.frame = d.first_frame
        d.velocity = calc_velocity(d.direction, dragon_direction, 5)
        d.X += d.velocity.x
        d.Y += d.velocity.y

        if d.X < 0 or d.X > screen_width - d.frame_width or d.Y < 0 or d.Y > screen_height - d.frame_height:
            reverse_direction(d, dragon_direction)
    pygame.draw.rect(screen, (50, 150, 50, 180), Rect(10, 10, player_health * 2, 25))
    pygame.draw.rect(screen, (100, 200, 100, 180), Rect(10, 10, 200, 2))
    player_group.draw(screen)
    dragon_group.draw(screen)
    pygame.display.update()
    screen.fill((40, 40, 40))