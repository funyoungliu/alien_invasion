import pygame.font
class Button():
    """按钮类"""
    def __init__(self,screen,ai_settings,msg):
        """设置按钮属性"""
        #获取屏幕
        self.screen=screen
        self.screen_rect=self.screen.get_rect()
        #设置按钮的大小
        self.width,self.height=200,50
        #设置按钮的颜色
        self.button_color=(0,255,0)
        #设置字体的颜色
        self.text_color=(255,255,255)
        #设置字体及大小
        self.font=pygame.font.SysFont(None,48)
        #获取按钮
        self.rect=pygame.Rect(0,0,self.width,self.height)
        #将按钮设置为屏幕中央
        self.rect.center=self.screen_rect.center
        #按钮标签只需创建一次
        self.prep_msg(msg)
    def prep_msg(self,msg):
        """获取按钮标签"""
        #将按钮渲染为图像，并使其在按钮上剧中
        self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center
    def draw_button(self):
        """绘制按钮"""
        #绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)