# -*- coding:utf8 -*-

import pygame, sys
from levels import levels
from sprite import *

def goto_next_level():
    global level
    level += 1
    if level > len(levels) - 1: level = 0
    load_level()

def update_blocks():
    global block_group, waiting
    if len(block_group) == 0:
        goto_next_level()
        waiting = True
    block_group.update(ticks, 50)

def load_level():
    global level, block_image, block_group
    block_image = pygame.image.load("Images/blocks.png").pygame.Surface.convert_alpha()
    block_group.empty()
    for bx in range(0, 12):
        for by in range(0, 10):
            num = levels[level][by*12+bx]
            if num > 0:
                block = MySprite()
                block.set_image(block_image, 58, 28, 3)
                x = 40 + bx * (block.frame_width + 1)
                y = 60 + by * (block.frame_height + 1)
                block.position = x, y
                block.first_frame = block.last_frame = num - 1
                block_group.add(block)

def game_init():
    global screen, font, timer
    global paddle_group, block_group, ball_group
    global paddle, block_image, block, ball_group
    global screen_width, screen_height

    screen_width = 800
    screen_height = 600
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Block Breaker Game")
    font = pygame.font.Font(None, 36)
    pygame.mouse.set_visible(False)
    timer = pygame.time.Clock()

    paddle_group = pygame.sprite.Group()
    block_group = pygame.sprite.Group()
    ball_group = pygame.sprite.Group()

    paddle = MySprite()
    paddle.load("Image/paddle.png")
    paddle.position = 400, 540
    paddle_group.add(paddle)

    ball = MySprite()
    ball.load("Image/ball.png")
    ball.position = 400, 300
    ball_group.add(ball)