#Advent of Code 2020 - Day 3

file = open("data.txt", "r")
slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
l=[]
for i in file.readlines():
    #Exclude newline
    l.append(i.replace('\n',''))

result = 1
for i in slopes:
    trees=0
    c=0
    for j in range(0, len(l), i[1]):
        if l[j][c%len(l[j])]=='#':
            trees+=1
        c+=i[0]
    result*=trees
print(result)