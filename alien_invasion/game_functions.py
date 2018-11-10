import pygame
import sys
from settings import Settings
from ship import Ships
from bullets import Bullets
from alien import Alien
from time import sleep
from game_stats import Game_stats
from button import Button
def check_events(screen,ai_settings,ship,bullets,aliens,game_stats,play_button,score_board):
    """监听游戏事件"""
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        #监听按键盘事件
        elif event.type==pygame.KEYDOWN:
            check_KEYDOWN_events(event,screen,ai_settings,ship,bullets,game_stats)
        #监听键盘抬起事件
        elif event.type==pygame.KEYUP:
            check_KEYUP_events(event,ship)
        #监听鼠标事件
        elif event.type==pygame.MOUSEBUTTONDOWN:
            #获取鼠标位置
            mouse_x,mouse_y=pygame.mouse.get_pos()
            #检查鼠标是否点击play按钮,并作出反应
            check_play_button(screen,ai_settings,ship,bullets,aliens,game_stats,play_button,mouse_x,mouse_y,score_board)
def check_KEYDOWN_events(event,screen,ai_settings,ship,bullets,game_stats):
    """监听按下键盘事件"""
    #按下右
    if event.key==pygame.K_RIGHT:
        ship.mviong_right=True
    #按下左
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True
    #按下空格
    elif event.key==pygame.K_SPACE and game_stats.game_stats:
        new_bullet=Bullets(screen,ai_settings,ship)
        if len(bullets)<=ai_settings.bullets_allowed:
            bullets.add(new_bullet)
    #按q结束游戏
    elif event.key==pygame.K_q:
        sys.exit()
def check_KEYUP_events(event,ship):
    if event.key==pygame.K_RIGHT:
        ship.mviong_right=False
    if event.key==pygame.K_LEFT:
        ship.moving_left=False
def check_play_button(screen,ai_settings,ship,bullets,aliens,game_stats,play_button,mouse_x,mouse_y,score_board):
    """检查是否鼠标是否点击play按钮，并作出相应反应"""
    if play_button.rect.collidepoint(mouse_x,mouse_y) and not game_stats.game_stats:
        #激活游戏
        game_stats.game_stats=True
        #初始化统计信息
        game_stats.reset_stats(ai_settings)
        #初始化游戏设置
        ai_settings.initialize_dynamic_settings()
        #清空外星人，子弹
        bullets.empty()
        aliens.empty()
        #飞船摆正
        ship.center_ship()
        #重新绘制一群外星人
        create_fleet(screen,ai_settings,ship,aliens)
        #隐藏光标
        pygame.mouse.set_visible(False)
        #重新绘制记分牌
        score_board.prep_score()
        score_board.prep_high_score()
        score_board.prep_level()
def get_number_aliens_x(ai_settings,alien):
    """计算一行能容纳多少个外星人"""
    alien_width=alien.rect.width
    #计算每行外星人的宽度
    available_space_x=ai_settings.screen_width-2*alien_width
    #计算每行可容纳多少个外星人
    number_aliens_x=int(available_space_x/(2*alien_width))
    return number_aliens_x
def get_number_aliens_y(ai_settings,ship,alien):
    """计算可以容纳多少行"""
    #计算容纳外星人的空白
    available_space_y=ai_settings.screen_height-3*alien.rect.height-ship.rect.height
    #计算可以容纳的行数
    number_aliens_y=int(available_space_y/(2*alien.rect.height))
    return number_aliens_y
def creat_alien(screen,ai_settings,alien_number_x,alien_number_y,aliens):
    """创建一个外星并把它加入编组"""
    alien=Alien(screen,ai_settings)
    #计算外星人的坐标
    alien_width=alien.rect.width
    alien_height=alien.rect.height
    alien.x=alien_width+2*alien_width*alien_number_x
    alien.rect.x=alien.x
    alien.y=alien_height+2*alien_height*alien_number_y
    alien.rect.y=alien.y
    aliens.add(alien)
def create_fleet(screen,ai_settings,ship,aliens):
    """在编组中添加外星人"""
    #计算每行可以容纳的外星人
    alien=Alien(screen,ai_settings)
    number_aliens_x=get_number_aliens_x(ai_settings,alien)
    number_aliens_y=get_number_aliens_y(ai_settings,ship,alien)
    #画出第一行外星人
    for alien_number_y in range(number_aliens_y):
        for alien_number_x in range(number_aliens_x):
            creat_alien(screen,ai_settings,alien_number_x,alien_number_y,aliens)
def check_edages(ai_settings,aliens):
    """检查是否外星人是否碰壁，如果碰壁则做调整"""
    for alien in aliens.sprites():
        if alien.check_edage():
            change_fleet_direction(ai_settings,aliens)
            break
def change_fleet_direction(ai_settings,aliens):
    """对外星人群进行调整"""
    #调整外星人的坐标
    ai_settings.aliens_direction*=-1
    for alien in aliens.sprites():
        alien.y+=alien.ai_settings.alien_drop_factor
        alien.rect.y=alien.y
def ship_hit(screen,ai_settings,ship,aliens,game_stats,score_board):
    """检测外星人是否撞上了飞船"""
    #停0.5秒，清空外星人，重新创造一批外星人，飞船摆正，飞船生命值-1
    aliens.empty()
    create_fleet(screen,ai_settings,ship,aliens)
    ship.center_ship()
    game_stats.ship_left-=1
    score_board.prep_ships()
    sleep(0.5)
def check_bottom(screen,aliens):
    """检测外星人是否到达屏幕的底部"""
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen_rect.bottom:
            print('触底')
            return True
            break
        else:
            return False
def update_aliens(screen,ai_settings,ship,aliens,game_stats,score_board):
    """更新外星人群的坐标"""
    check_edages(ai_settings,aliens)
    aliens.update(ai_settings)
    #检测外星人是否撞上了飞船或者外星人到达屏幕的底端
    if check_bottom(screen,aliens) or  pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(screen,ai_settings,ship,aliens,game_stats,score_board)
    #如果飞船剩余0架，则游戏处于停止状态
    if game_stats.ship_left==0:
        game_stats.game_stats=False
        pygame.mouse.set_visible(True)
def check_high_score(game_stats,score_board):
    """检查最高分"""
    if game_stats.score>=game_stats.high_score:
        game_stats.high_score=game_stats.score
        score_board.prep_high_score()
def check_collide(screen,ai_settings,ship,bullets,aliens,game_stats,score_board):
    """检查子弹和外星人是否发生碰撞"""
    #发生碰撞删除子弹和外星人
    collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
    #消灭一个外星人加分
    for aliens in collisions.values():
        game_stats.score+=ai_settings.alien_score*len(aliens)
        #检查是否为最高分
        check_high_score(game_stats,score_board)
        score_board.prep_score() 
    #如果外星人被全部消灭，则生成新的外星人并清空子弹，等级加1
    if len(aliens)==0:
        create_fleet(screen,ai_settings,ship,aliens)
        bullets.empty()
        ai_settings.increase_speed()
        game_stats.level+=1
        score_board.prep_level()
def update_bullets(screen,ai_settings,ship,bullets,aliens,game_stats,score_board):
    """更新子弹群的坐标"""
    #更新子弹的位置
    bullets.update()
    #消除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
    check_collide(screen,ai_settings,ship,bullets,aliens,game_stats,score_board)
def update_screen(screen,ai_settings,ship,bullets,aliens,game_stats,play_button,score_board):
    """更新屏幕"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    aliens.draw(screen)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    if game_stats.game_stats==False:
        play_button.draw_button()
    score_board.show_score()
    pygame.display.flip()   