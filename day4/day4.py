import sys
input =  [int(line) for line in open("day4/input.txt").readline().rstrip().split("-")]

def match(password, group_size_match_func):
    if len(password) != 6 or any(password[i] > password[i+1] for i in range(5)):
        return False
    groups = [password.count(ch) for ch in set(password)]
    return any(group_size_match_func(group) for group in groups)

print("Part 1: "+str(sum(match(str(pass_num), lambda x:x >= 2) for pass_num in range(input[0], input[1] + 1))))
print("Part 1: "+str(sum(match(str(pass_num), lambda x:x == 2) for pass_num in range(input[0], input[1] + 1))))