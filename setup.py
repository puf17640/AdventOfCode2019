import os
import sys
import datetime
import webbrowser

def setup(day):
  path = "./day"+str(day)
  if not os.path.exists(path):
    os.makedirs(os.path.realpath(path))
  if not os.path.exists(path+"/input.txt"):
    print("https://adventofcode.com/2019/day/"+str(day)+"/input")
  open(os.path.realpath(path+"/input.txt"), "a")
  if not os.path.exists(path+"/day"+str(day)+".py"):
    with open(os.path.realpath(path+"/day"+str(day)+".py"), "a") as f:
      f.write('input =  [line.rstrip() for line in open("day' + str(day) + '/input.txt").readlines()]')

if "today" in sys.argv:
  setup(datetime.datetime.today().day)
else:
  for day in range(1, 25):
    setup(day)
