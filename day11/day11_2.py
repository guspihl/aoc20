#Advent of Code 2020 - Day 11, Part 2

import itertools

def check_empty_adjacents(i,j):
    permutations = itertools.product([i-1,i,i+1],[j-1,j,j+1])
    for x,y in permutations:
        if x == i and y == j:
            continue
        if x < 0 or x >= len(l) or y < 0 or y >= len(l[x]):
            continue
        if l[x][y] == '#':
            return False
    return True

def check_occupied_adjacents(i,j):
    permutations = itertools.product([i-1,i,i+1],[j-1,j,j+1])
    n_occupied = 0
    n_empty = 0
    #check i+1 j+1 until out of bounds
    for x,y in permutations:
        if x == i and y == j:
            continue
        if x < 0 or x >= len(l) or y < 0 or y >= len(l[x]):
            n_empty += 1
            continue
        if l[x][y] == '#':
            n_occupied += 1
        else:
            n_empty += 1
        if n_occupied >= 5 or n_empty >= 4:
            break
    return True if n_occupied >= 5 else False

l = []
file = open("data.txt", "r")
for i in file.readlines():
    i = i.replace('\n','')
    l.append(i)

while True:
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

#Count number of occupied seats
occupied_seats = 0
for i in l:
    occupied_seats += i.count('#')

print("Part 1:", occupied_seats)


permutations = itertools.product(["i-1","i","i+1"],["j-1","j","j+1"])
a = list(permutations).remove(4)
print(a)