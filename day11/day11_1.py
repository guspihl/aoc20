#Advent of Code 2020 - Day 11

import itertools

def check_empty_adjacents(i,j):
    permutations = itertools.product([i-1,i,i+1],[j-1,j,j+1])
    for x,y in permutations:
        if x < 0 or x >= len(l) or y < 0 or y >= len(l[x]) or (x==i and j==y):
            continue
        if l[x][y] == '#':
            return False
    return True

def check_occupied_adjacents(i,j):
    permutations = itertools.product([i-1,i,i+1],[j-1,j,j+1])
    n_occupied = 0
    for x,y in permutations:
        if x < 0 or x >= len(l) or y < 0 or y >= len(l[x]) or (x==i and j==y):
            continue
        if l[x][y] == '#':
            n_occupied += 1
    return True if n_occupied >= 4 else False

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