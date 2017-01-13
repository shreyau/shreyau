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
