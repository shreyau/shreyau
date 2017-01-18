import re
import time
list_of_lines= []
src_f1=open("/home/asm/source.txt")
dest_f1=open("/home/asm/destination.txt")
list1= []
new=''
new1=''
dnew=''
dnew1=''
dict1={}
dict2={}
try:
 for line in src_f1:
   #print line
 
   res = re.search(r'(tempest.*)',line,re.I)
   if res:
     #print res.group()
     res1 = str(res.group())
     res2 = res1.split(' ... ')
     new=res2[0]
     new1=res2[1]
     #print new
     #print new1
     dict1[new]=new1
 
     #time.sleep(5)   
except IndexError:
	print dict1
     	print "error*************************************occurred"
	time.sleep(3)
'''-------------------------------------------------------------------------------------------'''
try:
 for line in dest_f1:
   #print line
   res = re.search(r'(tempest.[a-zA-Z](.*))',line,re.M|re.I)
   if res:
     #print res.group()
     res1 = str(res.group())
    # if res1:
     res2 = res1.split(' ... ')
     dnew=res2[0]
     dnew1=res2[1]
     #print dnew
     #print dnew1
     dict2[dnew]=dnew1
except IndexError:
        print dict2
     	print "error****occurred" 
#print res2[1]
     #list_of_lines.append(res2[0])
#print list_of_lines
#for n in list_of_lines:
 #         print n
#for n in list_of_lines:
   #print n
    
		     


