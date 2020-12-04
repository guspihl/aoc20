#Advent of Code 2020 - Day 4
def checkValid(k,v):
    eye_colours = ['amb','blu','brn','gry','grn','hzl','oth']
    if k=='byr':
        return int(v)>=1920 and int(v)<=2002
    elif k=='iyr':
        return int(v)>=2010 and int(v)<=2020
    elif k=='eyr':
        return int(v)>=2020 and int(v)<=2030
    elif k=='hgt':
        if v[-2:]=='cm':
            return int(v[:-2])>=150 and int(v[:-2])<=193
        elif v[-2:]=='in':
            return int(v[:-2])>=59 and int(v[:-2])<=76
    elif k=='hcl':
        return v[0]=='#' and len(v)==7
    elif k=='ecl':
        return v in eye_colours
    elif k=='pid':
        return len(v)==9
    elif k=='cid':
        return True
    else:
        return False


valid = 0
required = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
required = sorted(required)
l = []
passports = []
file = open("data.txt", "r")
for i in file.readlines():
    if i=='\n':
        passports.append(l)
        l = []
        continue
    for j in i.split():
        l.append(j)
passports.append(l)
l=[]

valid_passports = []
#Find all passports with all required fields.
for i in passports:
    for j in i:
        k,_=j.split(':')
        if k=='cid':continue
        l.append(k)
    if required==sorted(l):
        valid_passports.append(i)
    l=[]

for i in valid_passports:
    for j in i:
        k,v = j.split(':')
        if not checkValid(k,v):
            valid-=1
            break
    valid+=1

print("Part 1:",len(valid_passports))
print("Part 2:",valid)
