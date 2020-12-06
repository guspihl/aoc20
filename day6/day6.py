#Advent of Code 2020 - Day 6
l=[]
res=0
file = open("data.txt", "r")
for i in file.readlines():
    if i == '\n':
        for j in range(1,len(l)):
            l[0] = l[0].intersection(l[j])
        res+=len(l[0])
        l = []
    else:
        i = i.replace('\n','')
        l.append(set(i))
for j in range(1,len(l)):
    l[0] = l[0].intersection(l[j])
res+=len(l[0])
print(res)