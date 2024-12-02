
with open('day2/input.txt', 'r') as file:
    lines = [line.strip().split() for line in file]


file.close()
print(lines)

ans=0

for i, inner_list in enumerate(lines):
    Safe=True
    ascending=0
    for j, element in enumerate(inner_list):
        if j<len(inner_list)-1:
            value=int(inner_list[j])-int(inner_list[j+1])
            #print(int(inner_list[j]) ,int(inner_list[j+1]))
            if value>0:
                ascending=ascending+1
            if value<0:
                ascending=ascending-1
            if abs(value)>3 or value==0 or abs(ascending)!=j+1 :
                    Safe=False
                    print(inner_list,Safe,abs(ascending))
                    break
    if Safe:
        ans = ans+1

print(ans)
#Part B code was too messy