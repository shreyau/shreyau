from __future__ import division
def avg1(list1):
   for i in list1:
     sum1=0
     sum1=sum(list1)
     avg2=(sum1/(len(list1)-1))
   print sum1
   print avg2
list2= []
EOF="\n"  
print "enter elements of list"
while True:
  inp=input("enter number")
  list2.append(inp)
  if inp==0:
    break 
avg1(list2)
