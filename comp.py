import re
import time
import sys

src_f1=sys.argv[1]
dest_f1=sys.argv[2]
class Compare:
 def __init__(self,src_f1,dest_f1):
   self.src_f2=open(src_f1)
   self.dest_f2=open(dest_f1)
   self.f1=open("file1",'w+')                              #matching status same
   self.f2=open("file2",'w+')                              #matching status anything   
   self.f3=open("file3",'w+')                              #matching status differs  
   self.f4=open("file4",'w+')                              #lines present in first but not second
   self.f5=open("file5",'w+')                              #lines present in second but not in first  
   self.new=''
   self.new1=''
   self.dnew=''
   self.dnew1=''
   self.dict1={}
   self.dict2={}
   self.list1= []
   self.list2 = []         
   

 '''----------------------------------------------source file---------------------------------------'''
 def func(self):
  try:
   for line in self.src_f2:
    #print line
 
    res = re.search(r'(tempest.*)',line,re.I)
    if res:
      #print res.group()
      res1 = str(res.group())
      res2 = res1.split(' ... ')
      self.new=res2[0]
      self.new1=res2[1]
      new2=self.new1.strip('\r')
      #print new
      #print new2
      self.dict1[self.new]=new2
      s1=str(self.new)+' ... '+str(new2)
      self.list1.append(s1)
    
      #time.sleep(5)   
  except IndexError:
	#print dict1
	
     	print "error*************************************occurred"
	#time.sleep(3)
  '''--------------------------------------------dest file-----------------------------------------------'''
  try:
   for line in self.dest_f2:
     #print line
     res = re.search(r'(tempest.[a-zA-Z](.*))',line,re.M|re.I)
   
     if res:
       #print res.group()
       res1 = str(res.group())
     # if res1:
       res2 = res1.split(' ... ')
       self.dnew=res2[0]
       self.dnew1=res2[1]
       #print dnew
       #print dnew1
       self.dict2[self.dnew]=self.dnew1	
       s2=str(res2[0])+' ... '+str(res2[1])
       self.list2.append(s2)
 
  except IndexError:
        #print dict2
	print "error****occurred" 
  '''---------------------------------------------no of lines starting with tempest in src & dest file------------------''' 
  #print dict1.keys()
  #print dict2.keys()
  length=len(self.dict1)
  print "Total number of lines starting with 'tempest' in src file:'",length                         #2460
  length2=len(self.dict2)
  print "Total number of lines starting with 'tempest' in src file:'",length2                        #2059
  
  '''--------------------------------------------Matching status same-------------------------------------'''
  count=0
  count1=0
  print self.list1  
  print self.list2  

  for i in self.list1:
    for j in self.list2:
       if i==j:
           #print i
	   self.f1.writelines(i+'\n')
           count=count+1
           #print j
       
  self.f1.close()
  print "done"
  print "Total number of lines starting with 'tempest' to '...' matching status same:",count             #1663
 
  '''---------------------------------------------Matching Status anything--------------------------------'''
  '''countx=0
  county=0
  for key in dict1: 
   for jey in dict2:
     if key==jey:
        # print "match"
        # print key,"************",dict1[key]
	 s=str(key)+' ... '+str(dict1[key])
	 f2.writelines(s+'\n')
         #print s
	 #print "done"
	 #time.sleep(3)
         countx=countx+1
	# print jey,"++++++++++++++++"
         county=county+1
	 #print dict1[key]
         #print dict2[jey]
  print "wooooooooooooooooooooooo"
  print countx
  print county'''
 
  '''-----------------------------------------------Matching status anything part 2------------------------------'''
  count2=0
  count3=0
  for key in self.dict1:
     if (self.dict1[key]!='ok')&(self.dict1[key]!='FAIL'):    #&
       #print key,dict1[key]
       count2=count2+1
       self.f2.writelines(key+'\n')
  #f2.writelines("**********************************")
  print count2
	

  for jey in self.dict2:    
    if(self.dict2[jey]!='ok')&(self.dict2[jey]!='FAIL'):
     # print jey,dict2[jey]
      count3=count3+1
      self.f2.writelines(jey+'\n')
  print count3

  counts=count2+count3
  print "Total number of lines from 'tempest' to '...' matching status anything",counts
  self.f2.close()   
  '''---------------------------------------------------Matching status differs------------------------------------'''
  count3=0
  for key in self.dict1:
    for jey in self.dict2:
      if (key==jey):
         if(self.dict1[key]!=self.dict2[jey]): 
	     count3=count3+1
             self.f3.writelines(key+'\n')
 	    # print key,dict1[key]
	    # print jey,dict2[jey]  
  self.f3.close()
  print "Total number of lines starting with 'tempest' to '...' matching status differs:",count3      #221

  '''---------------------------------------------------tempest to ... in first but not second--------------------'''
  count4=0

  for key in self.dict1:
    if self.dict2.has_key(key):
     continue
    else:
      count4=count4+1
      self.f4.writelines(key+'\n')
      #print key
  print "doneee"
  print "Total number of lines starting with 'tempest' to '...' available in first not in second",count4    #576
  self.f4.close()

  '''----------------------------------------------------tempest to ... in second but not in first--------------------'''

  count5=0

  for jey in self.dict2:
    if self.dict1.has_key(jey):
     continue
    else:
     count5=count5+1
     self.f5.writelines(jey+'\n')
  print "yessssss"
  print "Total number of lines starting with 'tempest' to '...' available in second but not in first",count5  #175
  self.f5.close()

'''------------------------------------------------------------'''

a=Compare(src_f1,dest_f1)
a.func()







    
		     


