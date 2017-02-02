import MySQLdb
import smtplib
import getpass
localhost="localhost"
user="root"
password="root123"
database="employee"
db=MySQLdb.connect(localhost,user,password,database)
cursor=db.cursor()
print "connected"

cursor.execute("SELECT * FROM emp")
db.commit()
data=cursor.fetchall()
#print data
#s1 = 'Name\t\t\tAge\t\t\tEmpid\n'
cursor.execute("show columns from emp")
db.commit()
data1 = cursor.fetchall()
#print data1[0][0],data1[1][0],data1[2][0]
s1=data1[0][0]+'\t\t\t'+data1[1][0]+'\t\t\t'+data1[2][0]
s2=''
print s1
for i in data:
  s = '%s\t\t\t%s\t\t\t%s\n' % (i)
  s2=s2+s
  print s



host = "smtp.gmail.com"
port=587
server=smtplib.SMTP(host,port)
server.ehlo()
server.starttls()
server.ehlo()
username=raw_input("gmail")
password=getpass.getpass()
server.login(username,password)
to=raw_input("to")
sub=raw_input("sub")
mes=s1
mess=''
for line in s2:
 mess=mess+line
messs=mes+mess
message="subject: %s\n\n %s" %(sub,messs)
server.sendmail(username,to,message)

