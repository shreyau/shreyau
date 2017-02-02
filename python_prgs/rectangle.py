class Rect:
   def __init__(self,length,breadth):
     self.length = length
     self.breadth = breadth
   def area(self):
     return self.length*self.breadth
   def perimeter(self):
     return 2 * (self.length + self.breadth)
   def __add__(self,other):
     return self.area()+other.area()
rect1=Rect(5,4)
rect2=Rect(6,2)
print rect1.area()
print rect2.area()
print rect1.perimeter()
print rect2.perimeter()
print rect1.area()+rect2.area()
