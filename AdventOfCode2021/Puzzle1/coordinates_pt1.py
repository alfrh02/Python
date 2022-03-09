inputFile = open("input.txt", "r")

fileLines = inputFile.readlines()

depth = 0
horizontal_pos = 0

def detectCommand(command, param):
    global depth, horizontal_pos
    if command == "down":
        depth = depth + param
    elif command == "up":
        depth = depth - param
    elif command == "forward":
        horizontal_pos = horizontal_pos + param

for i in range(len(fileLines)):
    currentLine = i
    splitString = fileLines[currentLine].split(" ", 1)
    detectCommand(splitString[0], int(splitString[1]))
    
print(depth * horizontal_pos)