import pygame
from ship import Ships
from pygame.sprite import Group
class Scoreboard():
    """创建一个记分牌类"""
    def __init__(self,screen,ai_settings,game_stats):
        """初始化记分牌"""
        self.screen=screen
        self.screen_rect=self.screen.get_rect()
        self.ai_settings=ai_settings
        self.game_stats=game_stats
        #设置记分牌
        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,48)
        #将记分牌渲染为图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
    def prep_score(self):
        """将记分牌渲染为图像"""
        #积分牌的分数,并将得分圆整
        rounded_score=int(round(self.game_stats.score,-1))
        score_str="{:,}".format(rounded_score)
        self.score_image=self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)
        #设置记分牌的位置
        self.score_rect=self.score_image.get_rect()
        self.score_rect.top=20
        self.score_rect.right=self.screen_rect.right-20
    def prep_high_score(self):
        """将最高分渲染为图像"""
        rounded_high_score=int(round(self.game_stats.high_score,-1))
        high_score_str="{:,}".format(rounded_high_score)
        self.high_score_image=self.font.render(high_score_str,True,self.text_color,self.ai_settings.bg_color)
        #设置最高积分牌的位置
        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.top=self.score_rect.top
        self.high_score_rect.centerx=self.screen_rect.centerx
    def prep_level(self):
        """将等级渲染为图像"""
        level=str(self.game_stats.level)
        self.level_image=self.font.render(level,True,self.text_color,self.ai_settings.bg_color)
        self.level_image_rect=self.level_image.get_rect()
        self.level_image_rect.right=self.score_rect.right
        self.level_image_rect.top=self.score_rect.bottom+10
    def prep_ships(self):
        """将飞船渲染为图片"""
        self.ships=Group()
        #绘制剩下的飞船
        for ship_number in range(self.game_stats.ship_left):
            ship=Ships(self.screen,self.ai_settings)
            ship.rect.x=10+ship_number*ship.rect.width
            ship.rect.y=10
            self.ships.add(ship)
    def show_score(self):
        """绘制记分牌"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_image_rect)
        self.ships.draw(self.screen)