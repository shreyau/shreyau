def prime_num(*list1):
	print list1
	return list1

no=input("enter the range")
list2= []
for num in range(no):
  if num>1:
    for i in range(2,num):
	#print num
        if num%i==0:
         break
    else:
        list2.append(num)
	#print num
prime_num(list2)


***************************************************************************

from __future__ import division
def avg1(list1):
   for i in list1:
     sum1=0
     sum1=sum(list1)
     avg2=(sum1/len(list1))
   print sum1
   print avg2
list2= []  
print "enter elements of list"
while True:
  inp=input("enter number")
  list2.append(inp)
  if inp==00:
    break 
avg1(list2)

******************************************************************************

list1= []
while True:
  str1=raw_input()
  list1.append(str1)
  str2 = ''.join(list1)
  #print str2
  if str1=="EOF":
   break

print str2.swapcase()

**********************************************************************************
def sort1(list2):
   return list1
list1= []
while True:
  inp=raw_input()
  list1.append(inp)
  if inp=='end':
    break
  int(inp)
for i in range(len(list1)):
   for j in range(len(list1)-1):
     if list1[i]<list1[j]:
       t=list1[i]
       list1[i]=list1[j]
       list1[j]=t
list1.remove('end')
print list1
sort1(list1)
