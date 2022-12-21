file = open("Day4Input.txt")
data = file.read().split("\n")
contain = 0 # Part One
overlap = 0 # Part Two
for line in data:
    pair = line.split(",")
    aMin = int(pair[0].split("-")[0])
    aMax = int(pair[0].split("-")[1])
    bMin = int(pair[1].split("-")[0])
    bMax = int(pair[1].split("-")[1])
    if (bMin >= aMin and bMax <= aMax) or (aMin >= bMin and aMax <= bMax):
        contain += 1 # Part One
    if (bMin >= aMin and bMin <= aMax) or (aMin >= bMin and aMin <= bMax):
        overlap += 1 # Part Two
print("Containing: "+str(contain))
print("Overlapping: "+str(overlap))