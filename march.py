import random
'''
for i in range(32):
	print(i)
	print(random.randint(1,28))
	print("")
'''

R16Scores = [16, 22, 17, 16, 17, 8, 5, 8, 3, 3, 2, 7, 2, 1, 0, 1, 0]
R8Scores = [8, 18, 12, 8, 5, 1, 1, 3, 1, 3, 1, 3, 0, 0, 0, 0, 0]
R4Scores = [4, 11, 4, 3, 2, 1, 0, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0]
R2Scores = [2, 8, 1, 2, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
R1Scores = [1, 5, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def printFIRSTorSECOND(match, probfirst, probsecond, first, second):
    rand = random.randint(1, probfirst + probsecond)
    print(match)

    if rand <= probfirst:
        print(first, "\n")
        if first == second:
            print("FIRST")
        return first
    else:
        print(second, "\n")
        if first == second:
            print("SECOND")
        return second

print("ROUND OF 64")
R64Winners = []
for i in range(4):
    lst = []
    lst.append(printFIRSTorSECOND("1v16", 28, 0, 1, 16))
    lst.append(printFIRSTorSECOND("8v9", 14, 14, 8, 9))
    lst.append(printFIRSTorSECOND("5v12", 16, 12, 5, 12))
    lst.append(printFIRSTorSECOND("4v13", 23, 5, 4, 13))
    lst.append(printFIRSTorSECOND("6v11", 14, 14, 6, 11))
    lst.append(printFIRSTorSECOND("3v14", 23, 5, 3, 14))
    lst.append(printFIRSTorSECOND("7v10", 18, 10, 7, 10))
    lst.append(printFIRSTorSECOND("2v15", 26, 2, 2, 15))
    R64Winners.append(lst)

print("ROUND OF 32")
R32Winners = []
for i in range(4):
    lst = []
    for j in range(4):
        first = R64Winners[i][j*2]
        second = R64Winners[i][j*2 + 1]
        lst.append(printFIRSTorSECOND(str(first) + "v" + str(second), R16Scores[first], R16Scores[second], first, second))
    R32Winners.append(lst)

print("SWEET 16")
R16Winners = []
for i in range(4):
    lst = []
    for j in range(2):
        first = R32Winners[i][j*2]
        second = R32Winners[i][j*2 + 1]
        lst.append(printFIRSTorSECOND(str(first) + "v" + str(second), R8Scores[first], R8Scores[second], first, second))
    R16Winners.append(lst)

print("ELITE 8")
R8Winners = []
for i in range(4):
    first = R16Winners[i][0]
    second = R16Winners[i][1]
    R8Winners.append(printFIRSTorSECOND(str(first) + "v" + str(second), R4Scores[first], R4Scores[second], first, second))

print("FINAL 4")
R4Winners = []
for i in range(2):
    first = R8Winners[i*2]
    second = R8Winners[i*2+1]
    R4Winners.append(printFIRSTorSECOND(str(first) + "v" + str(second), R2Scores[first], R2Scores[second], first, second))

print("FINAL")
first = R4Winners[0]
second = R4Winners[1]
printFIRSTorSECOND(str(first) + "v" + str(second), R1Scores[first], R1Scores[second], first, second)


'''
temp = 0
while temp != -1:
    temp = int(input("Enter first: \n"))
    temp2 = int(input("Enter second: \n"))
    rand = random.randint(1,temp+temp2)
    if rand <= temp:
        print("FIRST")
    else:
        print("SECOND")
'''
