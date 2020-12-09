#Advent of Code 2020 - Day 9
l=[]
file = open("data.txt", "r")
for i in file.readlines():
    l.append(int(i))

for i in range(len(l)-25):
    b=False
    for k in range(i, i+25):
        for j in range(k+1,i+25):
            if l[k] != l[j] and l[k]+l[j]==l[i+25]:
                b=True
                break
    if not b:
        x = l[i+25]
        break
print("Part 1:",x)
for i in range(len(l)):
    for j in range(i+1,i+25):
        if sum(l[i:j]) == x:
            print("Part 2:",min(l[i:j])+max(l[i:j]))
            quit()