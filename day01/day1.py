#Advent of Code 2020 - Day 1

file = open("data.txt", "r")
l = []
for i in file.readlines():
    l.append(int(i))

for i in range(len(l)):
    for j in range(i+1,len(l)):
        for k in range(j+1, len(l)):
            if l[i]+l[j]+l[k]==2020:
                print(l[i]*l[j]*l[k])