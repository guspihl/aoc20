#Advent of Code 2020 - Day 11, Part 2

import itertools

def check_empty_adjacents(a,b):
    directions = itertools.product(["i-1","i","i+1"],["j-1","j","j+1"])
    for x,y in directions:
        if x == "i" and y == "j":
            continue
        i = a
        j = b
        i = eval(x)
        j = eval(y)
        while i >= 0 and i < len(l) and j >= 0 and j < len(l[i]):
            if l[i][j] == 'L':
                break
            elif l[i][j] == '#':
                return False
            i = eval(x)
            j = eval(y)
    return True

def check_occupied_adjacents(a,b):
    directions = itertools.product(["i-1","i","i+1"],["j-1","j","j+1"])
    n_occupied = 0
    for x,y in directions:
        if x == "i" and y == "j":
            continue
        i = a
        j = b
        i = eval(x)
        j = eval(y)
        while i >= 0 and i < len(l) and j >= 0 and j < len(l[i]):
            if l[i][j] == 'L':
                break
            elif l[i][j] == '#':
                n_occupied += 1
                break
            i = eval(x)
            j = eval(y)
    return True if n_occupied >= 5 else False

l = []
file = open("data.txt", "r")
for i in file.readlines():
    i = i.replace('\n','')
    l.append(i)

k=0
while True:
    print(k)
    for i in l:
        print(i)
    new_world = []
    state_changed = False
    for i in range(len(l)):
        line = ""
        for j in range(len(l[i])):
            if l[i][j] == 'L':
                if check_empty_adjacents(i,j):
                    line += '#'
                    state_changed = True
                else:
                    line += 'L'
            elif l[i][j] == '#':
                if check_occupied_adjacents(i,j):
                    line += 'L'
                    state_changed = True
                else:
                    line += '#'
            else:
                line += l[i][j]
        new_world.append(line)
    if not state_changed:
        break
    l = new_world
    k+=1

#Count number of occupied seats
occupied_seats = 0
for i in l:
    occupied_seats += i.count('#')

print("Part 2:", occupied_seats)