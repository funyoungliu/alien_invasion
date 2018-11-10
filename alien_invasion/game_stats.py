from scoreboard import Scoreboard
class Game_stats():
    def __init__(self,ai_settings):
        """初始化统计信息"""
        #初始化游戏的运行状态
        #将游戏的初始状态设为非活动状态
        self.game_stats=False
        self.score=0
        self.high_score=0
        #设置飞船等级
        self.level=1
        self.ai_settings=ai_settings
        self.reset_stats(ai_settings)
    def reset_stats(self,ai_settings):
        """初始化游戏运行期间可能变化的统计信息"""
        self.ship_left=ai_settings.ship_limit
        self.score=0
        self.level=1