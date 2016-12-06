"""
Day 3 of Advent of Code
Mohamed Lansari
"""

# all of the operational code for day3
def main():
    # all of the container variables
    tris = []

    # loop through and read all of the triangles
    # with open("info/day3info.txt", 'r') as f:
    #     for line in f:
    #         tri = []
    #         for word in line.split():
    #             tri.append(int(word))
    #         tris.append(tri)
    with open("info/day3info.txt", 'r') as f:
        # iterate by threes to split vertically
        i, lines = 0, []
        for line in f:
            # read in the line split
            lines.append(line.split())
            i += 1
            # check whether or not you need to format the triangles
            if i == 3:
                tris.append([int(lines[0][0]), int(lines[1][0]), int(lines[2][0])])
                tris.append([int(lines[0][1]), int(lines[1][1]), int(lines[2][1])])
                tris.append([int(lines[0][2]), int(lines[1][2]), int(lines[2][2])])
                i, lines = 0, []

    vTris = 0
    # iterate through the triangles and check and see which are valid
    for tri in tris:
        # find the largest element
        largest, ind = 0, -1
        for i in range(len(tri)):
            if tri[i] > largest:
                largest = tri[i]
                ind = i

        # add the other two
        inds = [0, 1, 2]
        inds.remove(ind)
        lesserSum = tri[inds[0]] + tri[inds[1]]

        # check and ensure that it's legitimate now
        if lesserSum > largest:
            vTris += 1

    print("Final amount of valid tris is ", vTris)

main()