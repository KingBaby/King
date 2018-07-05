# -*- coding:utf8 -*-

import pygame

def print_Text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen = pygame.display.get_surface()
    screen.blit(imgText,(x, y))

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "<x:%d, y:%d>" % (self.x, self.y)

class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.master_image = None
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 0
        self.frame_height = 0
        self.first_frame = 0
        self.last_frame = 0
        self.last_time = 0
        self.columns = 0
        self.direction = 0
        self.velocity = Point(0,0)

    def _getx(self): return self.rect.x
    def _setx(self, value): self.rect.x = value
    X = property(_getx, _setx)

    def _gety(self): return self.rect.y
    def _sety(self, value): self.rect.y = value
    Y = property(_gety, _sety)

    def _getpos(self): return self.rect.topleft
    def _setpos(self, value): self.rect.topleft = value
    position = property(_getpos, _setpos)

    def load(self, filename, width=0, height=0, columns=1):    # 为了与之前的代码兼容
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.set_image(self.master_image, width, height, columns)

    def set_image(self, image, width=0, height=0, columns=1):
        self.master_image = image
        if width == 0 and height == 0:
            self.frame_width = image.get_width()
            self.frame_height = image.get_height()
        else:
            self.frame_width = width
            self.frame_height = height
            rect = self.master_image.get_rect()
            self.last_frame =(rect.width // width) * (rect.height // height) - 1
        self.rect = pygame.Rect(0, 0, self.frame_width, self.frame_height)
        self.columns = columns

    def update(self, current_time, rate = 30):
        if self.last_frame >= self.first_frame:
            if current_time > self.last_time + rate:
                self.frame += 1
                if self.frame > self.last_frame or self.frame < self.first_frame:
                    self.frame = self.first_frame
                self.last_time = current_time

        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = pygame.Rect(frame_x, frame_y, self.frame_width, self.frame_height)
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame