"""
Day 1 of advent of code
Author:  Mohamed Lansari
"""

"""
Returns nothing

This runs the code necessary for day1
"""
def main():
    # take in the input string
    path = input()

    # strip the input of spaces
    path = path.replace(" ", "")
    # split along commas
    split = path.split(',')

    # run through each element
    d = 0       # 0 maps to North, 1 to East, 2 to South, 3 to West
    locX = 0
    locY = 0
    prevs = []
    hq = None
    for instruction in split:
        # split the instruction into the two parts
        delta = instruction[0]
        a = int(instruction[1:])

        # Rotate right if necessary
        if delta == "R":
            # turn right
            d += 1
            # wrap back around if necessary
            d = d % 4

        # Rotate left if necessary
        elif delta == "L":
            # turn left
            d -= 1
            # wrap back around if necessary
            if (d < 0):
                d = 3

        # Move by a spaces, as instructed
        for i in range(a):
        # change location amount
            if d == 0:
                # locY += int(a)
                locY += 1
            elif d == 1:
                # locX += int(a)
                locX += 1
            elif d == 2:
                # locY -= int(a)
                locY -= 1
            elif d == 3:
                # locX -= int(a)
                locX -= 1

            # Add this current coordinate pair to the map of coordinate pairs and instances
            coord = (locX, locY)
            if coord in prevs:
                hq = coord
                break
            else:
                prevs.append(coord)

        # Make sure we don't overwrite the previous hq info'
        if hq is not None:
            break

    # add up to return the shortest path
    print(abs(hq[0]) + abs(hq[1]))
    print("Headquarters is at: ", hq, ", a distance away of ", abs(hq[0]) + abs(hq[1]))


main()
