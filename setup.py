import os
import datetime
import webbrowser

day = datetime.datetime.today().day
path = "./day"+str(day)
if not os.path.exists(path):
  os.makedirs(os.path.realpath(path))
if not os.path.exists(path+"/input.txt"):
  print("https://adventofcode.com/2019/day/"+str(day)+"/input")
open(os.path.realpath(path+"/input.txt"), "a")
open(os.path.realpath(path+"/day"+str(day)+".py"), "a")