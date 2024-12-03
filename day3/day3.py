import re
from math import *

S = open('day3/input.txt').read()


ans1 = 0
for i in range(len(S)):
    #time to brush up on regex ;)
    match = re.match("mul\((\d+),(\d+)\)", S[i:])
    if match is not None:
        ans1=ans1+int(match.group(1))*int(match.group(2))

print(ans1)