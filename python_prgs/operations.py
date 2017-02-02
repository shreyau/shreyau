class Class1:
   def __init__(self,a):
     self.a=a
     print "obj oriented"
   def __str__(self):
     return str(self.a)

   def __del__(self):
     print "obj remove"

   def sqr(self):
     return self.a**2

   def __add__(self,other):
     return self.a+other.a

   def __sub__(self,other):
     return self.a-other.a

   def __mul__(self,other):
     return self.a*other.a

   def __div__(self,other):
     return self.a/other.a



b=Class1(10)   
a=Class1(20)
print a+b
print a-b
print a*b
print a/b
#print b
print b.sqr()
del b
