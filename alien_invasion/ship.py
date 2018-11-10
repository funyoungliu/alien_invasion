import pygame
from settings import Settings
from pygame.sprite import Sprite
class Ships(Sprite):
    """飞船类"""
    def __init__(self,screen,ai_settings):
        """初始化飞船并初始化飞船的位置"""
        super().__init__()
        self.screen=screen
        self.screen_rect=self.screen.get_rect()
        self.image=pygame.image.load('files/python/ship.bmp')
        self.rect=self.image.get_rect()

        #将每艘飞船放在屏幕的底部
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        #飞船的移动指标
        self.moving_left=False
        self.mviong_right=False

        #飞船的精确位置
        self.ai_settings=ai_settings
        self.center=float(self.rect.centerx)
    def center_ship(self):
        self.center=self.screen_rect.centerx
    def update(self):
        if self.mviong_right and self.rect.right<self.screen_rect.right:
            self.center+=self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>self.screen_rect.left:
            self.center-=self.ai_settings.ship_speed_factor
        self.rect.centerx=self.center
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)