import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    """创建外星人类"""
    def __init__(self,screen,ai_settings):
        """创建一个外星人，并初始化其位置"""
        super(Alien,self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        self.image=pygame.image.load('files/python/alien.bmp')
        self.rect=self.image.get_rect()
        #初始化外星人的位置
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        #得到外星人的精确位置
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)
        self.direction_x=1
        self.direction_y=0
    def check_edage(self):
        """检查外星人是否到达了屏幕边缘"""
        #检查外星人是否到达了屏幕的右边缘
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        #检查外星人是否到达了屏幕的左边缘
        elif self.rect.left<=0:
            return True
    def update(self,ai_settings):
        """更新外星人的位置"""
        #更新外星人的横坐标
        self.x+=ai_settings.aliens_direction*self.ai_settings.alien_speed_factor
        self.rect.x=self.x
    def blitme(self):
        """绘制外星人"""
        self.screen.blit(self.image,self.rect)

