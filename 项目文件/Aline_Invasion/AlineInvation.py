import sys

import pygame

from settings import Settings

from ship import Ship

class AlineInvation:
    """管理游戏资源"""
    
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width , self.settings.screen_height))
        pygame.display.set_caption("Aline Invation")
        self.ship = Ship(self)
        
    def run_game(self):
        """开始主循环"""
        while True:
            # 监听鼠标和键盘事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #重新绘制屏幕颜色
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            #刷新游戏窗口的显示
            pygame.display.flip()
            
            
            
if __name__ == '__main__':
    ai = AlineInvation()
    ai.run_game()