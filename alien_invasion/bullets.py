import pygame
from pygame.sprite import Sprite
class Bullets(Sprite):
    """一个对飞船发射的子弹进行管理的类"""
    def __init__(self,screen,ai_setting,ship):
        """在飞船所处的位置创建一个子弹对象"""
        super().__init__()
        self.screen=screen
        self.rect=pygame.Rect(0,0,ai_setting.bullets_width,ai_setting.bullets_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        self.y=float(self.rect.y)
        self.color=ai_setting.bullets_color
        self.speed_factor=ai_setting.bullets_speed_factor
    def update(self):
        self.y-=self.speed_factor
        self.rect.y=self.y
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)