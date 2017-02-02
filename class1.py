#class1.py.py
#file parsing using object oriented programming
#inserting data into the database
#!/usr/bin/python


import re
import sys
import mysql.connector
import time

#for row in data :
 #   print row[:]
in_file=open("/home/asm/diag.out")
conn = None
cursor = None
query = None
class Work:
 def __init__(self,in_file):
   self.conn = mysql.connector.connect(
         user='root',
         password='root',
         host='localhost',
         database='access')
   print("database connected")
   self.cursor = self.conn.cursor(buffered=True)
   self.query = ("SELECT * FROM acc")
   self.cursor.execute(query)
  # data = cursor.fetchall ()
   print "obj oriented"
 def __del__(self):
  print "obj removed"
 def func(self):
  #in_file=open("/home/asm/diag.out")
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
  for ap in aps:
	print ap
  print "added"

  for ap in aps:
	mac = re.search(r'([0-9A-F]{2}[:-]){5}([0-9A-F]{2})', ap, re.I)                                       #mac
	ipv4 = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ap,re.I)                                       #ipv4
	ipv6 = re.search(r'([0-9a-f]{1,4})::[0-9]{1}',ap,re.I)                                                #ipv6
        name = re.search(r'(Name\s.*)',ap,re.I)                                                               #name
        tunnel_sec = re.search(r'(Tunnel/Sec Mode\s.*)',ap,re.I)                                              #tunnel and sec_mode
	state = re.search(r'(State\s.*)(\s)(:)\s([0-9a-zA-Z]{1,3}){1}?',ap,re.I)                              #State
	mesh = re.search(r'(Mesh Role\s.*)',ap,re.I)                                                          #mesh role
	psk = re.search(r'(PSK)(\s*):\s(.*)',ap,re.I)                                                         #PSK
	timer = re.search(r'(Timer\s.*)',ap,re.I)                                                             #timer
        hw_sw = re.search(r'(HW/SW Version\s.*)',ap,re.I)                                                     #Hw/SW version
	mod_ser = re.search(r'(Model/Serial Num\s.*)',ap,re.I)                                                #model/serial
	if mac:             
            print "++++",mac.group()           #mac
	   
	if ipv4:
	    print ipv4.group()                #ipv4
	    
        if ipv6:
            print ipv6.group()                #ipv6 
           
        if name:
	    #print name.group()               #name line
	    name1 = str(name.group())
            name2 = name1.split(': ')
           # print name2[0]
            print name2[1]                   #name value
           
  	if tunnel_sec:
	    print tunnel_sec.group()
	    tunnel_sec1 = str(tunnel_sec.group())
            tunnel_sec2 = tunnel_sec1.split(':')
           # print tunnel_sec2[0]          #tunnelsec mode line
           # print tunnel_sec2[1]          #value of tunnel and sec mode
            tunnel_sec3 = tunnel_sec2[1].split('/')
            print tunnel_sec3[0]          #tunnel value
            print tunnel_sec3[1]          #sec mode value
	
	if state:
           # print state.group()
	    state1=str(state.group())
	    state2=state1.split(':')
            print state2[1]               #State=Run
	if mesh:
           # print mesh.group()
	    mesh1=str(mesh.group())
            mesh2=mesh1.split(':')
            print mesh2[1]               #Mesh role = MESH AP/ROOT AP
	if psk:   
	    #print psk.group()
	    psk1=str(psk.group())
            psk2=psk1.split(': ')
            print psk2[1]                #PSK
	if timer:
            #print timer.group() 
            timer1=str(timer.group())
            timer2=timer1.split(':')
            print timer2[1]             #Timer
	    timer3=timer2[1].split('in ')
            print timer3[1]
	if hw_sw:
           # print hw_sw.group()
            hw_sw1=str(hw_sw.group())
            hw_sw2=hw_sw1.split(':')
            print hw_sw2[1]
            hw_sw3=hw_sw2[1].split('/')
            print hw_sw3[0]              #HW VERSION
            print hw_sw3[1]              #SW VERSION
	if mod_ser:
           # print mod_ser.group()
            mod_ser1=str(mod_ser.group())
            mod_ser2=mod_ser1.split(':')
            print mod_ser2[1]
            mod_ser3=mod_ser2[1].split('/')
            print mod_ser3[0]           #model
            print mod_ser3[1]           #serial number
        if mac and ipv4 and ipv6 and name and tunnel_sec and state and mesh and psk and timer and hw_sw and mod_ser:
             query1= "insert into acc(MACAddress,IPV4Address,IPV6Address,Name,State,Tunnel,Sec_Mode,Mesh_Role,PSK,Timer,HW_Version,SW_Version,Model,Serial_Number) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" % (mac.group(),ipv4.group(),ipv6.group(),name2[1],state2[1],tunnel_sec3[0],tunnel_sec3[1],mesh2[1],psk2[1],timer3[1],hw_sw3[0],hw_sw3[1],mod_ser3[0],mod_ser3[1])
             self.cursor.execute(query1)
             self.conn.commit()
       


  print "value added"

a=Work(in_file)
a.func()
print a
   	





	
	

   



   





























