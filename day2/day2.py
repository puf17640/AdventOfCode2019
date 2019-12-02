input_list = [int(op) for op in open("day2/input.txt").readline().split(",")]

def run(noun, verb):
  inp = input_list[:]
  inp[1], inp[2], pointer = noun, verb, 0
  while pointer < len(inp):
    if inp[pointer] == 1:
      inp[inp[pointer+3]] = inp[inp[pointer+1]]+inp[inp[pointer+2]]
      pointer+=4
    elif inp[pointer] == 2:
      inp[inp[pointer+3]] = inp[inp[pointer+1]]*inp[inp[pointer+2]]
      pointer+=4
    elif inp[pointer] == 99:
      return inp[0]
    else:
      return -1

print("Part 1: "+str(run(12,2)))

for noun in range(100):
  for verb in range(100):
    if run(noun, verb) == 19690720:
      print("Part 2: "+str(100*noun+verb))
