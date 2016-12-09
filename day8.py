"""
Day 8 of Advent of Code
Mohamed Lansari
"""

# main code goes here
def main():
    # lines of input
    lines = []

    with open('info/day8info.txt', 'r') as f:
        for line in f:
            lines.append(line.strip())

    # create the basic rectangle info
    rect = [["." for i in range(50)] for i in range(6)]
    # read through input
    for line in lines:
        info = line.split(" ")
        
        # Rect creation logic
        if info[0] == "rect":
            dim = info[1].split("x")
            for i in range(int(dim[1])):
                for j in range(int(dim[0])):
                    rect[i][j] = "#"
    
        elif info[0] == "rotate":
            # decide whether to rotate row or column
            if info[1] == "row":
                rect = rotRow(rect, int(info[2].split("=")[1]), int(info[4]))
            elif info[1] == "column":
                rect = rotCol(rect, int(info[2].split("=")[1]), int(info[4]))
    
    # count amount of lit pixels
    count = 0
    for i in rect:
        for j in i:
            if j == "#":
                count += 1
    
    printRect(rect)
    print(count, "pixels lit")

def rotRow(rect, y, amount):
    newRow = list(rect[y])
    for i in range(len(rect[y])):
        newRow[(i + amount) % 50] = rect[y][i]
    rect[y] = newRow
    return rect


def rotCol(rect, x, amount):
    newCol = ["." for i in range(6)]
    for i in range(6):
        newCol[(i + amount) % 6] = rect[i][x]
    for i in range(len(newCol)):
        rect[i][x] = newCol[i]
    return rect

def printRect(rect):
    for row in rect:
        for pix in row:
            print(pix, end=" ")
        print()

main()