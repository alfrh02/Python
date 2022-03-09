import os

inputFile = open("input.txt", "r")
fileLines = inputFile.readlines()

increaseCounter = 0

for i in range(len(fileLines)):
    prevLine = i - 1
    currentLine = i
    # print(int(fileLines[currentLine]))
    if int(fileLines[currentLine]) > int(fileLines[prevLine]):
        increaseCounter = increaseCounter + 1

print(increaseCounter)