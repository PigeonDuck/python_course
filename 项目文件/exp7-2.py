class Block:
    # Good Luck!
    def __init__(self,WLH):
        self.WLH = WLH
    def get_width(self):
        return self.WLH[0]
    def get_length(self):
        return self.WLH[1]
    def get_height(self):
        return self.WLH[2]
    def get_volume(self):
        return self.WLH[0]*self.WLH[1]*self.WLH[2]
    def get_surface_area(self):
        area=self.WLH[0]*self.WLH[1]*2
        area1 =self.WLH[1]*self.WLH[2]*2
        area2 = self.WLH[0]*self.WLH[2]*2
        return area+area1+area2
    

block = Block([2,4,6])

print(block.get_width())
print(block.get_length())
print(block.get_height())
print(block.get_volume())
print(block.get_surface_area())