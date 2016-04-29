#!/usr/bin/env python2
# -*- coding:utf8 -*-

'''
简介: 这个是学习《python游戏编程入门》这本书的第二章
pie game游戏的代码，git的不同分支将代表不同步骤。
作者: King
时间: 2016/2/23

相关配置:
运行系统: archlinux
python版本: python2.7.11
pygame版本: pygame1.9.1

git的master分支是hello world程序，
drawsomething分支是绘制图形，
pigame分支是完整的piegame程序
'''
#接下来，开始写绘制图形的程序。
#第一步，导入pygame库。
import pygame
import sys
#第二步，导入pygame中所有的常量。
from pygame.locals import *
import math

#第三步，初始化pygame，就可以访问库中所有的资源
pygame.init()

#第四步，获取一个窗口并设置宽高
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption('The Pie Game - Press 1,2,3,4')
myfont = pygame.font.Font(None, 60)

color = 200, 80, 60
width = 4
x = 300
y = 250
radius = 200
position = x-radius, y-radius, radius*2, radius*2

piece1 = False
piece2 = False
piece3 = False
piece4 = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

        elif event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_1:
                piece1 = True
            elif event.key == pygame.K_2:
                piece2 = True
            elif event.key == pygame.K_3:
                piece3 = True
            elif event.key == pygame.K_4:
                piece4 = True

    #clear the screen
    screen.fill((0, 0, 200))

    #draw the four numbers
    testImg1 = myfont.render("1", True, color)
    screen.blit(testImg1, (x+radius/2-20, y-radius/2))
    testImg2 = myfont.render("2", True, color)
    screen.blit(testImg2, (x-radius/2, y-radius/2))
    testImg3 = myfont.render("3", True, color)
    screen.blit(testImg3, (x-radius/2, y+radius/2-20))
    testImg4 = myfont.render("4", True, color)
    screen.blit(testImg4, (x+radius/2-20, y+radius/2-20))

    #should the pieces be drawn?
    if piece1:
        start_angle = math.radians(0)
        end_angle = math.radians(90)
        pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
        pygame.draw.line(screen, color, (x, y), (x, y-radius), width)
        pygame.draw.line(screen, color, (x, y), (x+radius, y), width)
    if piece2:
        start_angle = math.radians(90)
        end_angle = math.radians(180)
        pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
        pygame.draw.line(screen, color, (x, y), (x, y-radius), width)
        pygame.draw.line(screen, color, (x, y), (x-radius, y), width)
    if piece3:
        start_angle = math.radians(180)
        end_angle = math.radians(270)
        pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
        pygame.draw.line(screen, color, (x, y), (x-radius, y), width)
        pygame.draw.line(screen, color, (x, y), (x, y+radius), width)
    if piece4:
        start_angle = math.radians(270)
        end_angle = math.radians(360)
        pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
        pygame.draw.line(screen, color, (x, y), (x, y+radius), width)
        pygame.draw.line(screen, color, (x, y), (x+radius, y), width)

    #is the pie finished?
    if piece1 and piece2 and piece3 and piece4:
        color = 0, 255, 0
    pygame.display.update()

