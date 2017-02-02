from os import walk
import os
import os.path, time
import datetime as dt
from datetime import datetime
now = dt.datetime.now()
ago = now-dt.timedelta(days=30)

print ago

#for file in os.listdir("/home/asm"):
  #print file
 
for file in os.listdir("/home/asm"):
    s=dt.datetime.fromtimestamp(os.path.getctime(file))
    #print s
    if s<ago:
      print file
     
f = []
for (dirpath, dirnames, filenames) in walk("/home/asm/test"):
    f.extend(filenames)
print f  


