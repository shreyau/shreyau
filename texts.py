#!/usr/bin/python
import re
import sys
import mysql.connector
import time
conn = mysql.connector.connect(
         user='root',
         password='root',
         host='localhost',
         database='access')
print("database connected")
cursor = conn.cursor(buffered=True)
query = ("SELECT * FROM acc")
cursor.execute(query)
data = cursor.fetchall ()
for row in data :
    print row[:]
#cursor.close()   #close cursor object
#conn.close()  #close connection object
in_file=open("/home/asm/diag.out")
list_of_lines= []
for line in in_file:
        res = re.match("----- APmgr info: apmgrinfo -a", line , re.M|re.I)
        if res:
          for line in in_file:
            list_of_lines.append(line)
            res1 = re.match("----- Disconnected APs: wlaninfo --all-disc-ap -l 3", line , re.M|re.I)
            if res1:
               break
in_file.close()
for n in list_of_lines:
    	print(n)
	if n == "\n":
		print "_________________________"
aps = []
ap = []
for line in list_of_lines:
	
	if line != "\n":
		ap.append(line)
	else:
		ap = "".join(ap)
		aps.append(ap)
		ap = [] 
print len(aps)
#regex = r"(^(\s*)^[a-zA-Z]+.*)"
#regex= r"[(^\s*)(Name)(\s*)(: )(.*)( $)]"
a=b=c=d=e=f=g=h=i=j=k=l=0
for ap in aps:
	
	print ap
	#print "_______________________"
	#pass	
	#print ap[8:25]
	mac=ap[8:25]
	#print ap[28:43]
	ipv4=ap[28:43]
 	#print ap[45:53]
	ipv6=ap[44:53]
	#print ap[75:91]
        #Name=ap[75:91]
	#print ap[111:133]
	#cursor.execute("insert into acc values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(mac,ipv4,ipv6,Name,b,c,d,e,f,g,h,i,k,l))
        #cursor.execute(query2)
        conn.commit() 
	#conn.rollback()
print "added"

for ap in aps:
	var = re.search(r'([0-9A-F]{2}[:-]){5}([0-9A-F]{2})', ap, re.I)       #mac
	var1 = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ap,re.I)         #ipv4
	var2 = re.search(r'([0-9a-f]{1,4})::[0-9]{1}',ap,re.I)                 #ipv6
        var3 = re.search(r'(:)\s([0-9a-zA-Z]{1,10}[-][0-9A-Za-z]{1,10})?([0-9a-zA-Z]){1,10}',ap,re.I)         #name
        var4 = re.search(r'([0-9a-zA-Z]{1,2}\s[(][A-Za-z]{1,7}[)]\s[/]\s[a-zA-Z]{1,3})+',ap,re.I)             #tunnel and sec_mode
	var5 = re.search(r'(State\s.*)(\s)(:)\s([0-9a-zA-Z]{1,3}){1}?',ap,re.I)                               #State
	var6 = re.search(r'(Mesh Role\s.*)',ap,re.I)                            #mesh role
	var7 = re.search(r'(PSK)(\s*):\s(.*)',ap,re.I)                          #PSK
	var8 = re.search(r'(Timer\s.*)',ap,re.I)                                #timer
        var9 = re.search(r'(HW/SW Version\s.*)',ap,re.I)                        #Hw/SW version
	var10 = re.search(r'(Model/Serial Num\s.*)',ap,re.I)
	#var=re.search(r"([^\s*](a-zA-Z)+[\s*](: )(.*))]",ap,re.M|re.I)
	if var:             
            print "++++",var.group()
	   # query1 = "insert into acc(MACAddress) values('%s');" % var.group()
            #cursor.execute(query1)                                                                 #[^Name]\s.*
	    #conn.commit()
	if var1:
	    print var1.group()
	    #query3 = "insert into acc(IPV4Address) values('%s');" % var1.group()
	   # print query1
            # Execute the SQL command
            #cursor.execute(query3)
	    #conn.commit()
        if var2:
            print var2.group()
           # query2= "insert into acc(IPV6Address) values('%s');" % var2.group
           # cursor.execute(query2)
           # conn.commit() 
        if var3:
	    print var3.group() 
	    var31 = re.search(r'(\s.*:)',ap,re.I)
            #if var31:
		#print var31.group() 
	   # query4 = "insert into acc(Name) values('%s') ;" % var3.group()
          #  cursor.execute(query4)
           # conn.commit()
	      #time.sleep(3)
  	if var4:
	   # print var4.group()
	    var41 = str(var4.group())
            var42 = var41.split('/')
            print var42[0]          #tunnel
            print var42[1]          #sec_mode
	if var5:
           # print var5.group()
	    var51=str(var5.group())
	    var52=var51.split(':')
            print var52[1]          #State=Run
	if var6:
           # print var6.group()
	    var61=str(var6.group())
            var62=var61.split(':')
            print var62[1]          #Mesh role = MESH AP/ROOT AP
	if var7:
	    #print var7.group()
	    var71=str(var7.group())
            var72=var71.split(': ')
            print var72[1]          #PSK
	if var8:
            #print var8.group() 
            var81=str(var8.group())
            var82=var81.split(':')
            print var82[1]          #Timer
	if var9:
           # print var9.group()
            var91=str(var9.group())
            var92=var91.split(':')
            print var92[1]
            var93=var92[1].split('/')
            print var93[0]          #HW VERSION
            print var93[1]          #SW VERSION
	if var10:
            print var10.group()
            var101=str(var10.group())
            var102=var101.split(':')
            print var102[1]
            var103=var102[1].split('/')
            print var103[0]        #model
            print var103[1]        #serial number
        if var and var1 and var2 and var3 and var4:
             query1= "insert into acc(MACAddress,IPV4Address,IPV6Address,Name,State,Tunnel,Sec_Mode,Mesh_Role,PSK,Timer,HW_Version,SW_Version,Model,Serial_Number) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" % (var.group(),var1.group(),var2.group(),var3.group(),var42[0],var42[1],var52[1],var62[1],var72[1],var82[1],var93[0],var93[1],var103[0],var103[1])
             cursor.execute(query1)
             conn.commit()



print "value added"
   	





	
	

   



   





























