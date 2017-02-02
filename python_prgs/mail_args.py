import smtplib
import getpass
import sys
host = "smtp.gmail.com"
port=587
server=smtplib.SMTP(host,port)
server.ehlo()
server.starttls()
server.ehlo()
username=raw_input("gmail")
password=getpass.getpass()
server.login(username,password)
to=sys.argv[1]
sub=sys.argv[3]
mes=sys.argv[2]
mes1=open(mes)
mes2=mes1.read()
message="subject: %s\n\n %s" %(sub,mes2)
server.sendmail(username,to,message)

