#Advent of Code 2020 - Day 1

file = open("data.txt", "r")

p1 = 0
p2 = 0
for i in file.readlines():
    i = i.split()
    lower, upper = map(int,i[0].split('-'))
    ch = i[1][0]
    if i[2].count(ch) >= lower and i[2].count(ch) <= upper:
        p1+=1
    if (i[2][lower-1] == ch)^(i[2][upper-1] == ch):
        p2+=1

print("Part 1:",p1,"\nPart 2:",p2)