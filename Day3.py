def getVal(c):
    if not c.isupper():
        return(ord(c) - 96)
    return(ord(c) - 38)

file = open("Day3Input.txt")
data = file.read().split("\n")
# Part One
prioritySum = 0
for line in data:
    a = line[:int(len(line)/2)]
    b = line[int(len(line)/2):]
    highest = 0
    for char in a:
        if char in b:
            prioritySum += getVal(char)  
print("Priority Sum: "+str(prioritySum))
# Part Two
badgeSum = 0
for i in range(0, len(data)-2, 3):
    a = data[i]
    b = data[i+1]
    c = data[i+2]
    for char in a:
        if char in b and char in c:
            badgeSum += getVal(char)
            break
print("Badge Sum: "+str(badgeSum))