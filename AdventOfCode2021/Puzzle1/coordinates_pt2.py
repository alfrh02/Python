inputFile = open("input.txt", "r")

fileLines = inputFile.readlines()

depth = 0
horizontal_pos = 0
aim = 0

def detectCommand(command, param):
    global depth, horizontal_pos, aim
    if command == "down":
        aim += param
    elif command == "up":
        aim -= param
    elif command == "forward":
        horizontal_pos += param
        depth += aim * param

for i in range(len(fileLines)):
    currentLine = i
    splitString = fileLines[currentLine].split(" ", 1)
    detectCommand(splitString[0], int(splitString[1]))
    
print(depth * horizontal_pos)