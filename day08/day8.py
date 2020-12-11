#Advent of Code 2020 - Day 8

def check_termination_path(instruction,executed,index):
    acc = 0
    terminated = False
    if instruction[0] == 'nop':
        instruction[0] = 'jmp'
        idx = index + int(instruction[1])
    else:
        instruction[0] == 'nop'
        idx = index+1

    while idx not in executed:
        if idx >= len(l):
            terminated = True
            break
        instruction = l[idx].split()
        executed.append(idx)
        if instruction[0] == 'acc':
            acc += int(instruction[1])
        
        elif instruction[0] == 'jmp':
            idx += int(instruction[1])
            continue

        idx += 1
    return terminated, acc


l=[]
file = open("data.txt", "r")
for i in file.readlines():
    l.append(i.replace('\n',''))

executed_instructions = []
idx = 0
accumulator = 0
while True:
    if idx >= len(l):
        print("Program terminated correctly with accumulator:", accumulator)
        break
    instruction = l[idx].split()
    executed_instructions.append(idx)
    if instruction[0] == 'acc':
        accumulator += int(instruction[1])
    
    elif instruction[0] == 'jmp':
        terminated, accs = check_termination_path(instruction,executed_instructions,idx)
        if terminated:
            print("Program terminated with accumulator:", accs+accumulator)
            part2 = accs+accumulator
            break
        idx += int(instruction[1])
        continue
    
    elif instruction[0] == 'nop':
        terminated, accs = check_termination_path(instruction,executed_instructions,idx)
        if terminated:
            print("Program terminated with accumulator:", accs+accumulator)
            part2 = accs+accumulator
            break
    idx += 1