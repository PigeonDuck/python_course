
class Vector:

    def __init__(self,vector):
        self.vector = vector

    def equals(self,vector2):
       if len(self.vector)!=len(vector2.vector): return False
       for i in range(0, len(self.vector)):
           if self.vector[i] !=vector2.vector[i]:
            return False
       return True
    
    def __str__(self):
        return str(tuple(self.vector)).replace(" ", "")
    
    def add(self,vector2):
       if len(self.vector)!=len(vector2.vector): raise Exception()
       result=[]
       for i in range(0,len(self.vector)):
         result.append(vector2.vector[i]+self.vector[i])
       
       x = Vector(result)
       return x
    
    def subtract(self,vector2):
       if len(self.vector)!=len(vector2.vector): raise Exception()
       result=[]
       for i in range(0,len(self.vector)):
         result.append(-(vector2.vector[i]-self.vector[i]))

       x = Vector(result)
       return x
    
    def dot(self,vector2):
       if len(self.vector)!=len(vector2.vector): raise Exception()
       self.result=[]
       sum = 0
       for i in range(0,len(self.vector)):
         self.result.append(vector2.vector[i]*self.vector[i])
         sum = sum +self.result[i]
       return sum
    
    def norm(self):
       sum = 0
       for i in range(0,len(self.vector)):
         sum = sum +self.vector[i]**2
       return (sum)**0.5
    
    def __str__(self):
        return str(tuple(self.vector)).replace(" ", "")
    
    

# a = Vector([1, 2, 3])
# b = Vector([3, 4, 5])
# c = Vector([5, 6, 7, 8])
# print(a.add(b))      # should return a new Vector([4, 6, 8])
# print(a.subtract(b)) # should return a new Vector([-2, -2, -2])
# print(a.dot(b))      # should return 1*3 + 2*4 + 3*5 = 26
# print(a.norm())      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
# #print(a.add(c))      # raises an exception
# print(a.subtract(b).equals(Vector([-2, -2, -2])))