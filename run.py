import sys
import os
import datetime

if "today" in sys.argv:
  day = datetime.datetime.today().day
  print("Day "+str(day)+":")
  os.system("python3 "+os.path.realpath("./day"+str(day)+"/day"+str(day)+".py"))
else:
  for day in range(1, 25):
    if(os.path.exists(os.path.realpath("./day"+str(day)+"/day"+str(day)+".py"))):
      if day > 1: 
        print()
      print("Day "+str(day)+":")
      os.system("python3 "+os.path.realpath("./day"+str(day)+"/day"+str(day)+".py"))