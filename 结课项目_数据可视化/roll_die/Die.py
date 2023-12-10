from random import randint

class Die:

    def __init__(self,num_sides=6):  #骰子有6个面
        self.num_sides = num_sides   #数据初始化
       
    def roll(self):  #用于投掷骰子
        return randint(1,self.num_sides)   #随机返回1到6的点数 [1,6]
    

    
