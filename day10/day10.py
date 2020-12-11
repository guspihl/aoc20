#Advent of Code 2020 - Day 10

l = [0]
file = open("data.txt", "r")
for i in file.readlines():
    l.append(int(i))
l = sorted(l)
one_jolt_diff = 0
three_jolt_diff = 1

for i in range(len(l)-1):
    if l[i]+1 == l[i+1]:
        one_jolt_diff += 1
    elif l[i]+3 == l[i+1]:
        three_jolt_diff += 1
print("Part 1:",one_jolt_diff*three_jolt_diff)

i=0
paths = 1

#The number of paths depending on how many differences of 1s there is in a row is determined by the
#tribonacci sequence. In the test-cases of this challenge, there is never more than 4 consecutive
#differences of 1, so I chose the lazy way of calculating the number of paths.
while i < len(l):
    if i+4 < len(l) and l[i]+4 == l[i+4]:
        paths *= 7
        i += 4
    elif i+3 < len(l) and l[i]+3 == l[i+3]:
        paths *= 4
        i += 3
    elif i+2 < len(l) and l[i]+2 == l[i+2]:
        paths *= 2
        i += 2
    else:
        i += 1
print("Part 2:",paths)


#1 2 4 7 11?