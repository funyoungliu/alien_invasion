import pygame
import sys
from settings import Settings
from ship import Ships
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import Game_stats
from button import Button
from scoreboard import Scoreboard
def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('外星人入侵')
    ship=Ships(screen,ai_settings)
    #创建一个子弹编组
    bullets=Group()
    #创建一个外星人编组
    aliens=Group()
    #在编组中添加外星人
    gf.create_fleet(screen,ai_settings,ship,aliens)
    #创建一个游戏状态的用例
    game_stats=Game_stats(ai_settings)
    #创建一个button用例
    play_button=Button(screen,ai_settings,'play')
    #创建一个记分牌的用例
    score_board=Scoreboard(screen,ai_settings,game_stats)
    #开始游戏的主循环
    while True:
        #监听键盘和鼠标事件
        gf.check_events(screen,ai_settings,ship,bullets,aliens,game_stats,play_button,score_board)
        #游戏处于运行状态时，以下功能才运行
        if game_stats.game_stats:
                #更新飞机的位置
                ship.update()
                #更新子弹
                gf.update_bullets(screen,ai_settings,ship,bullets,aliens,game_stats,score_board)
                #更新外星人
                gf.update_aliens(screen,ai_settings,ship,aliens,game_stats,score_board)
                #绘制最近的屏幕 
        gf.update_screen(screen,ai_settings,ship,bullets,aliens,game_stats,play_button,score_board)
run_game()