# -*- coding:utf8 -*-

import pygame, sys
from levels import levels
from sprite import MySprite, Point, print_Text

game_over = False
waiting = True
score = 0
lives = 100
level = 0

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
    block_image = pygame.image.load("Images/blocks.png").convert_alpha()
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
    global paddle, block_image, block, ball
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
    paddle.load("Images/paddle.png")
    paddle.position = (screen_width + paddle.frame_width) / 3, screen_height - paddle.frame_height - 10
    paddle_group.add(paddle)

    ball = MySprite()
    ball.load("Images/ball.png")
    ball.position = 400, 300
    ball_group.add(ball)

def move_paddle():
    global movex, movey, keys, waiting, screen_width
    paddle_group.update(ticks, 50)
    if keys[pygame.K_SPACE]:
        if waiting:
            waiting = False
            reset_ball()
    elif keys[pygame.K_LEFT]: paddle.velocity.x = -10
    elif keys[pygame.K_RIGHT]: paddle.velocity.x = 10
    else:
        if movex < -2: paddle.velocity.x = movex
        elif movex > 2: paddle.velocity.x = movex
        else:
            paddle.velocity.x = 0
    paddle.X += paddle.velocity.x
    if paddle.X < 0: paddle.X = 0
    elif paddle.X > screen_width: paddle.X = screen_width - paddle.frame_width
    
def reset_ball():
    ball.velocity = Point(4.5, -7.0)

def move_ball():
    global waiting, ball, game_over, lives
    ball_group.update(ticks, 50)
    if waiting:
        ball.X = paddle.X + paddle.frame_width / 2.0
        ball.Y = paddle.Y - ball.frame_height
    ball.X += ball.velocity.x
    ball.Y += ball.velocity.y
    if ball.X < 0:
        ball.X = 0
        ball.velocity.x *= -1
    elif ball.X > screen_width - ball.frame_width:
        ball.X = screen_width - ball.frame_width
        ball.velocity.x *= -1
    if ball.Y < 0:
        ball.Y = 0
        ball.velocity.y *= -1
    elif ball.Y > screen_height:
        waiting = True
        lives -= 1
        if lives < 1: game_over = True
    
def collision_ball_paddle():
    if pygame.sprite.collide_rect(ball, paddle):
        ball.velocity.y = -abs(ball.velocity.y)
        bx = ball.X
        by = ball.Y
        px = paddle.X + paddle.frame_width / 2
        py = paddle.Y + paddle.frame_height / 2
        if bx < px:
            ball.velocity.x = -abs(ball.velocity.x)
        else:
            ball.velocity.x = abs(ball.velocity.x)

def collision_ball_blocks():
    global score, block_group, ball
    hit_block = pygame.sprite.spritecollideany(ball, block_group)
    if hit_block != None:
        score += 10
        block_group.remove(hit_block)
        bx = ball.X + 8
        by = ball.Y + 8
        if bx > hit_block.X + ball.frame_width and \
            bx < hit_block.X + hit_block.frame_width - ball.frame_width:
            if by < hit_block.Y + hit_block.frame_height / 2:
                ball.velocity.y = -abs(ball.velocity.y)
            else:
                ball.velocity.y = abs(ball.velocity.y)
        elif bx < hit_block.X + ball.frame_width:
            ball.velocity.x = -abs(ball.velocity.x)
        elif bx > hit_block.X + hit_block.frame_width - ball.frame_width:
            ball.velocity.x = abs(ball.velocity.x)
        else:
            ball.velocity.y *= -1

game_init()
load_level()

while True:
    timer.tick(30)
    ticks = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            movex, movey = 0, 0#event.rel
        elif event.type == pygame.MOUSEBUTTONUP:
            if waiting:
                waiting = False
                reset_ball()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:
                goto_next_level()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        sys.exit()
    if not game_over:
        update_blocks()
        move_paddle()
        move_ball()
        collision_ball_paddle()
        collision_ball_blocks()
    
    screen.fill((40, 40, 40))

    print_Text(font, 0, 0, "LEVEL: %d" % (level+1))
    print_Text(font, screen_width / 4, 0, "BALLS: %d" % lives)
    print_Text(font, screen_width / 2, 0, "SCORE: %d" % score)

    block_group.draw(screen)
    ball_group.draw(screen)
    paddle_group.draw(screen)
    if game_over:
        gameover_shadow = pygame.image.load("Images/GAMEOVER_shadow_800_600.png").convert_alpha()
        screen.blit(gameover_shadow, (0, 0))
        print_Text(font, screen_width/3, screen_height/2, "G A M E  O V E R")

    pygame.display.update()
    