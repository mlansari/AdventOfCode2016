"""
Day 2 of Advent of Code
Mohamed Lansari
"""

# create the reference dictionaries
# up = {1:1, 2:2, 3:3, 4:1, 5:2, 6:3, 7:4, 8:5, 9:6}
# down = {1:4, 2:5, 3:6, 4:7, 5:8, 6:9, 7:7, 8:8, 9:9}
# left = {1:1, 2:1, 3:2, 4:4, 5:4, 6:5, 7:7, 8:7, 9:8}
# right = {1:2, 2:3, 3:3, 4:5, 5:6, 6:6, 7:8, 8:9, 9:9}
up = {1:1, 2:2, 3:1, 4:4, 5:5, 6:2, 7:3, 8:4, 9:9, "A":6, "B":7, "C":8, "D":"B"}
down = {1:3, 2:6, 3:7, 4:8, 5:5, 6:"A", 7:"B", 8:"C", 9:9, "A":"A", "B":"D", "C":"C", "D":"D"}
left = {1:1, 2:2, 3:2, 4:3, 5:5, 6:5, 7:6, 8:7, 9:8, "A":"A", "B":"A", "C":"B", "D":"D"}
right = {1:1, 2:3, 3:4, 4:4, 5:6, 6:7, 7:8, 8:9, 9:9, "A":"B", "B":"C", "C":"C", "D":"D"}

# main code for it all
def main():
    # create base info variables
    keystr, currKey, lines = '', 5, []
    
    # loop through lines in the input file, and read them into a list
    with open("info/day2info.txt", 'r') as f:
        for line in f:
            lines.append(line)

    # loop through each line
    for l in lines:
        # strip the endline from it
        lf = l.strip("\n")

        # run through each character instruction
        for key in lf:
            # decide what to do based on which key it is
            if key is "U":
                currKey = up[currKey]
            elif key is "R":
                currKey = right[currKey]
            elif key is "L":
                currKey = left[currKey]
            elif key is "D":
                currKey = down[currKey]
        
        # add the final key to the combination
        keystr = ''.join([str(keystr), str(currKey)])

    print(keystr)

main()