#!/bin/env python2
# -*- coding:utf8 -*-

import sys, math, random, pygame
from pygame.locals import *
from datetime import datetime, date, time

def print_text(font, x, y, text, color=(255, 255, 255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))

def wrap_angle( angle ):
    return angle % 360

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Analog Clock Demo")
font = pygame.font.Font(None, 36)

orange = 220,180, 0
white = 255, 255, 255
yellow = 255, 255, 0
pink = 255, 100, 100

pos_x = 300
pos_y = 250
radius = 250
angle = 360

#repeating loop
while True:
    for event in pygame.event.get():
        if event == QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    screen.fill((0, 0, 100))

    pygame.draw.circle(screen, white, (pos_x, pos_y), radius, 6)

    #draw the clock number 1-12
    for n in range(1, 13):
        angle = math.radians(n*360/12 - 90)
        x = math.cos(angle) * (radius-20) - 10
        y = math.sin(angle) * (radius-20) - 10
        print_text(font, pos_x+x, pos_y+y, str(n))

    #get the time of day
    today = datetime.today()
    hours = today.hour % 12
    minutes = today.minute
    seconds = today.second

    #darw the hours hand
    hours_angle = wrap_angle(hours * (360/12) - 90)
    hours_angle = math.radians( hours_angle )
    hour_x = math.cos( hours_angle ) * (radius-80)
    hour_y = math.sin( hours_angle ) * (radius-80)
    target = (pos_x+hour_x, pos_y+hour_y)
    pygame.draw.line(screen, pink, (pos_x, pos_y), target, 25)

    #darw the minutes hand
    min_angle = wrap_angle(minutes * (360/60) - 90)
    min_angle = math.radians( min_angle )
    min_x = math.cos( min_angle ) * (radius-60)
    min_y = math.sin( min_angle ) * (radius-60)
    target = (pos_x+min_x, pos_y+min_y)
    pygame.draw.line(screen, orange, (pos_x, pos_y), target, 12)

    #darw the hours hand
    seconds_angle = wrap_angle(seconds * (360/60) - 90)
    seconds_angle = math.radians( seconds_angle )
    sec_x = math.cos( seconds_angle ) * (radius-40)
    sec_y = math.sin( seconds_angle ) * (radius-40)
    target = (pos_x+sec_x, pos_y+sec_y)
    pygame.draw.line(screen, yellow, (pos_x, pos_y), target, 6)

    pygame.draw.circle(screen, white, (pos_x, pos_y), 20)
    print_text(font, 0, 0, str(hours) + ':' + str(minutes) + ':' + str(seconds))
    pygame.display.update()
