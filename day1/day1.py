with open('day1/input.txt', 'r') as file:
    l, r = map(list, zip(*(line.split() for line in file)))
    #zip makes tuples out of two iterators
    #we split each line of input.txt, and use zip to "pair them up" into tuples.
    #map runs a function with iterable arguments
    #We run the list constructor and turn all tuples into lists l and r (left and right)
    
file.close()

#sort ascending
l.sort()
r.sort()

ans=0
ansB=0

for a, b in zip(l, r):
#with zip we can iterate through two lists simultaniously
    ans += abs(int(a) - int(b))
    ansB += int(a)*r.count(a)
    #r.count(a) = How many times a is found in list r

print(ans)
print(ansB)