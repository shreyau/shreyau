import random
class Matrix:
    def __init__(self):
        self.mat = []
    def givnum(self):
        n=input("enter range")            #range of matrix
        for i in range(n):                #values of 1st matrix
          row=[]
          for j in range(n):
             data=input()
             row.append(data)
          self.mat.append(row)
          print self.mat

    def __add__(self,b):
        mat=[]
        for j in range(len(self.mat)):
            temp=[]            
            for k in range(len(self.mat[0])):
                x=self.mat[j][k] + b.mat[j][k]
                temp.append(x)
            mat.append(temp)
            rez=mat
        return rez
    def __sub__(self,b):
        mat=[]
        for j in range(len(self.mat)):
            temp=[]            
            for k in range(len(self.mat)):
                x=self.mat[j][k] - b.mat[j][k]
                temp.append(x)
            mat.append(temp)            
        return mat       

a=Matrix()
b=Matrix()

#a.print_matrix()
a.givnum()
b.givnum()

print a+b
print b-a
#print a*b

