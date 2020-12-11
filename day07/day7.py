#Advent of Code 2020 - Day 7

def find_bag(bag:str)->bool:
    v = bags[bag]
    result = []
    if "no other bags." in v:
        return False
    else:
        for i in v:
            if i[1] == 'shiny gold':
                return True
            else:
                result.append(find_bag(i[1]))
        return True if True in result else False

def count_bags(bag):
    v = bags[bag]
    res = []
    if "no other bags." in v:
        return 0
    else:
        for i in v:
            res.append(i[0] + i[0] * count_bags(i[1]))
        return sum(res)

bags = {}
file = open("data.txt", "r")

#Improvable data cleansing
for i in file.readlines():
    i = i.replace("\n","")
    i = i.split(' contain ')
    key = i[0][:-5]
    
    if i[1] == "no other bags.":
        bags[key] = [i[1]]
        continue

    values = i[1].split(', ')
    l=[]
    for j in values:
        x = j.split()
        amount = int(x[0])
        bag = x[1] + ' ' + x[2]
        l.append([amount,bag])
    bags[key] = l

n_bags = 0
for i in bags:
    if i == "shiny gold":continue
    values = bags[i]
    for j in values:
        if j == 'no other bags.':
            break
        elif j[1] == 'shiny gold':
            n_bags += 1
            break
        elif find_bag(j[1]):
            n_bags += 1
            break

print("Number of bags that lead to a shiny gold bag:",n_bags)
print("Shiny gold bag contains",count_bags('shiny gold'),"bags.")


