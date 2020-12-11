#Advent of Code 2020 - Day 5
l=[]
file = open("data.txt", "r")
for i in file.readlines():
    row = i[:7].replace('B','1').replace('F','0')
    seat = i[7:10].replace('R','1').replace('L','0')
    l.append(int(row,2)*8+int(seat,2))
    
l=sorted(l)
print("Highest seat ID:",l[-1])
for i in range(len(l)):
    if l[i]+1 != l[i+1]:
        print("Missing seat:",l[i]+1)
        break