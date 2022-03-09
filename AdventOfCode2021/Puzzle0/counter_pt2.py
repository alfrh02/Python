import os
#import time

inputFile = open("input.txt", "r")
fileLines = inputFile.readlines()

increaseCounter = 0
prevSlidingWindow = 10000

for i in range(len(fileLines)):
    prevLine = i - 1
    currentLine = i
    nextLine = i + 1
    secondNextLine = i + 2

    try:
        slidingWindow = int(fileLines[currentLine]) + int(fileLines[nextLine]) + int(fileLines[secondNextLine])
    except:
        print(increaseCounter)
    
    print(f"Line {i} + {nextLine} + {secondNextLine} = {slidingWindow}")

    #time.sleep(1)

    if slidingWindow > prevSlidingWindow:
        increaseCounter = increaseCounter + 1

    prevSlidingWindow = slidingWindow

print(increaseCounter)