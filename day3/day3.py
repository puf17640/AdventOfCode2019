import math
input =  [line.rstrip().split(",") for line in open("day3/input.txt").readlines()]

DX = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
DY = {'L': 0, 'R': 0, 'U': 1, 'D': -1}
def get_points(A):
  x = 0
  y = 0
  length = 0
  ans = {}
  for cmd in A:
    d = cmd[0]
    n = int(cmd[1:])
    assert d in ['L', 'R', 'U', 'D']
    for _ in range(n):
      x += DX[d]
      y += DY[d]
      length += 1
      if (x,y) not in ans:
        ans[(x,y)] = length
  return ans

l1 = get_points(input[0])
l2 = get_points(input[1])
both = set(l1.keys()) & set(l2.keys())
print("Part 1: "+str(min(abs(x)+abs(y) for (x,y) in both)))
print("Part 2: "+str(min(l1[p]+l2[p] for p in both)))

