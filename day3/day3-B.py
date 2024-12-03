import re
from math import *

S = open('day3/input.txt').read()

def mul(x,y):
  return x*y

ans2 = 0
enabled = True

for i in range(len(S)):
  if re.match(r"^do\(\)", S[i:]):
        enabled = True
  if re.match(r"^don't\(\)", S[i:]):
        enabled = False
  match = re.match("mul\((\d+),(\d+)\)", S[i:])
  #print(instr2)
  if match is not None and enabled:
    ans2=ans2+int(match.group(1))*int(match.group(2))
    #print(match)
        #p1=p1+int(instr.group(1))*int(instr.group(2))

print(ans2)