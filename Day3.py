file = open("Day3Input.txt")
data = file.read().split("\n")
prioritySum = -52
for line in data:
    a = line[:int(len(line)/2)]
    b = line[int(len(line)/2):]
    highest = 0
    for c in a:
        if c in b:
            if ord(c) >= 97:
                val = ord(c) - 70
            else:
                val = ord(c) - 64
            if val > highest:
                highest = val
                print("Priority: "+c)
    prioritySum += highest
            
print("Priority Sum: "+str(prioritySum))