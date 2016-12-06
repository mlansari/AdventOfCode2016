"""
Day 6 of Advent of Code
Mohamed Lansari
"""
import operator

# primary code location
def main():
    # list of lines of transmissions
    lines = []

    # read the data file
    with open('info/day6info.txt', 'r') as f:
        for line in f:
            l = line.strip()
            lines.append(l)

    # iterate through each letter in the length of the first line
    letters = []
    for i in range(len(lines[0])):
        letterDict = {}
        # iterate through each line to count
        for line in lines:
            # put the letter in the dict
            if line[i] in letterDict.keys():
                letterDict[line[i]] += 1
            else:
                letterDict[line[i]] = 1

        # sort letterDict
        primesort = sorted(letterDict.items(), key=operator.itemgetter(0))
        # sort = sorted(primesort, key=operator.itemgetter(1), reverse=True)    # part 1
        sort = sorted(primesort, key=operator.itemgetter(1))                    # part 2
        letters.append(sort[0][0])

    # print out the final letters
    print(''.join(letters))

main()