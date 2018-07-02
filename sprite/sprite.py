# -*- coding:utf-8 -*-

import pygame

class MySprite(pygame.sprite.Sprite):
    def __init__(self, target):
        pygame.sprite.pygame.sprite.Sprite.__init__(self)
        self.master_image = None
        self.frame = 0                                      # 第几个图像
        self.old_frame = -1                                 # 上一个图像
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0                                # 第一个图像
        self.last_frame = 0                                 # 最后一个图像
        self.columns = 1
        self.last_time = 0                                  # 记录上一次时间，用于控制时间间隔

    # X property
    def _getx(self):
        return self.rect.x
    def _setx(self, value):
        self.rect.x = value
    X = property(_getx, _setx)

    # Y property
    def _gety(self):
        return self.rect.y
    def _sety(self, value):
        self.rect.y = value
    Y = property(_gety, _sety)

    #position property
    def _getpos(self):
        return self.rect.topleft
    def _setpos(self, pos):
        self.rect.topleft = pos
    position = property(_getpos, _setpos)

    def load(self, filename, width, height, columns):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.frame_width = width
        self.frame_height = height
        self.rect = pygame.Rect(150, 150, width, height)
        self.columns = columns
        rect = self.master_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) - 1

    def update(self, current_time, rate = 30):
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time

        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = pygame.Rect(frame_x, frame_y, self.frame_width, self.frame_height)
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame

    def __str__(self):
        return "last_frame:%d-first_frame:%d-last_frame:%d-frame_width:%d-frame_height:%d-" % \
                (self.frame, self.first_frame, self.last_frame, self.frame_width, self.frame_height) +\
               "columns:%d-" % (self.columns) + str(self.rect)
