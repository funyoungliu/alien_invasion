class Settings:
    def __init__(self):
        #设置屏幕参数
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)
        #设置飞船参数
        self.ship_speed_factor=1.5
        self.ship_limit=3
        #设置子弹参数
        self.bullets_speed_factor=1
        self.bullets_width=5
        self.bullets_height=15
        self.bullets_color=(60,60,60)
        self.bullets_allowed=5
        #设置外星人参数
        self.alien_speed_factor=1
        self.alien_drop_factor=10
        self.aliens_direction=1
        self.alien_score=50
        #游戏速度参数
        self.speedup_scale=1.5
    def initialize_dynamic_settings(self):
        """初始化游戏参数"""
        self.ship_speed_factor=1.5
        self.bullets_speed_factor=1
        self.alien_speed_factor=1
        self.alien_drop_factor=10
        self.aliens_direction=1
        self.alien_score=50
    def increase_speed(self):
        """加速游戏"""
        self.ship_speed_factor*=self.speedup_scale
        self.bullets_speed_factor*=self.speedup_scale
        self.alien_speed_factor*=self.speedup_scale
        self.alien_drop_factor*=self.speedup_scale
        self.alien_score*=self.speedup_scale