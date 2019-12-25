import math
import functools

input =  [math.floor(int(line.replace("\n", ""))/3)-2 for line in open("day1/input.txt").readlines()]
print("Part 1: "+str(int(functools.reduce(lambda x,y: x+y, input))))

def accumulate(y):
  x = 0
  while True: 
    y = int(math.floor(y/3)-2)
    if y < 0: 
      return x
    x = x+y

print("Part 2: "+str(int(functools.reduce(lambda x,y: x+y, [i+accumulate(i) for i in input]))))