file = open("Day1Input.txt")
data = file.read().split("\n")
max = 0
current = 0
for line in data:
    if line != "":
        current += int(line)
    else:
        if current > max:
            max = current
        current = 0
print("Highest: "+str(max))
one = 0
two = 0
three = 0
current = 0
for line in data:
    if line != "":
        current += int(line)
    else:
        if current > one:
            three = two
            two = one
            one = current
        elif current > two:
            three = two
            two = current
        elif current > three:
            three = current
        current = 0
print("Top Three: "+str(one+two+three))