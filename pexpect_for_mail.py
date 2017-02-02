#for run this we will use gmail_sample.py


import pexpect
import sys
m = pexpect.spawn('python gmail_sample.py')
m.logfile_read = sys.stdout
m.expect("Username:")
m.sendline("shreyuspecial28@gmail.com")
m.expect("Password:")
m.sendline("76239790149705")
m.expect("To address :")
m.sendline("tejaskumarnj@gmail.com")
m.expect("Subject :")
m.sendline("test")
m.expect("Enter the content. Your last line should be as 'end'")
m.sendline("hello")
m.sendline("end")
m.expect("test has been send to a.gopikrishna01@gmail.com")
m.close()
