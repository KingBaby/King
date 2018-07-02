# -*- coding:utf-8 -*-

import pygame

def print_text(font, x, y, text, color=(255, 255, 255)):
    imgText = pygame.font.render(text, True, color)
    screen = pygame.display.get_surface()
    screen.blit(imgText, (x, y))

class Point(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getx(self): return self.__x
    def setx(self, value): self.__x = value
    x = property(getx, setx)

    def gety(self): return self.__y
    def sety(self, value): self.__y = value
    y = property(gety, sety)

    def __str__(self):
        return "{X: %d, Y: %d}" % (self.__x, self.__y)

class MySprite(pygame.sprite.Sprite):
    def __init__(self):
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
        self.direction = 0
        self.velocity = Point(0, 0)

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

class Direction(object):
    def __init__(self, north = 0, east= 0, south = 0, west = 0, northeast = 0, southeast = 0, southwest = 0, northwest = 0):
        self.__north = north
        self.__east = east
        self.__south = south
        self.__west = west
        self.__northeast = northeast
        self.__northwest = northwest
        self.__southeast = southeast
        self.__southwest = southwest

    def _getnorth(self): return self.__north
    def _setnorth(self, value): self.__north = value
    north = property(_getnorth, _setnorth)

    def _getsouth(self): return self.__south
    def _setsouth(self, value): self.__south = value
    south = property(_getsouth, _setsouth)

    def _geteast(self): return self.__east
    def _seteast(self, value): self.__east = value
    east = property(_geteast, _seteast)

    def _getwest(self): return self.__west
    def _setwest(self, value): self.__west = value
    west = property(_getwest, _setwest)

    def _getnortheast(self): return self.__northeast
    def _setnortheast(self, value): self.__northeast = value
    northeast = property(_getnortheast, _setnortheast)

    def _getnorthwest(self): return self.__northwest
    def _setnorthwest(self, value): self.__northwest = value
    northwest = property(_getnorthwest, _setnorthwest)

    def _getsoutheast(self): return self.__southeast
    def _setsoutheast(self, value): self.__southeast = value
    southeast = property(_getsoutheast, _setsoutheast)

    def _getsouthwest(self): return self.__southwest
    def _setsouthwest(self, value): self.__southwest = value
    southwest = property(_getsouthwest, _setsouthwest)

    def __str__(self):
        return "<north:%d, northeast:%d, east:%d, southeast:%d, south:%d, southwest:%d, west:%d, northwest:%d>"