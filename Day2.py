# Part One
file = open("Day2Input.txt")
data = file.read().split("\n")
fails = ["C Y", "A Z", "B X", "C B", "A C", "B A"]
ties = ["C Z", "A X", "B Y", "C C", "A A", "B B"]
def calcScore():
    score = 0
    for line in data:
        if line in ties:
            score += 3
        elif not line in fails:
            score += 6
        if line[-1] == "X" or line[-1] == "A":
            score += 1
        elif line[-1] == "Y" or line[-1] == "B":
            score += 2
        elif line[-1] == "Z" or line[-1] == "C":
            score += 3
    return(score)
print("Final Score: "+str(calcScore()))

# Part Two
def findLoser(string):
    alphabet = 'ABC'
    for c in alphabet:
        if string + c in fails:
            return(string + c)
    return(string + string[0])

def findWinner(string):
    alphabet = 'ABC'
    for c in alphabet:
        if string + c not in fails and string + c not in ties:
            return(string + c)
    return(string + string[0])

for i in range(len(data)):
    if data[i][-1] == "X":
        data[i] = findLoser(data[i][:-1])
    elif data[i][-1] == "Y":
        data[i] = data[i][:-1] + data[i][0]
    elif data[i][-1] == "Z":
        data[i] = findWinner(data[i][:-1])
print("Actual Score: "+str(calcScore()))