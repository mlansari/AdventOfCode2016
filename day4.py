"""
Day 4 of Advent of Code
Mohamed Lansari
"""
import operator

letterMap = {0:"a", 1:"b", 2:"c", 3:"d", 4:"e", 5:"f", 6:"g", 7:"h", 8:"i", 9:"j", 10:"k",
             11:"l", 12:"m", 13:"n", 14:"o", 15:"p", 16:"q", 17:"r", 18:"s", 19:"t", 20:"u",
             21:"v", 22:"w", 23:"x", 24:"y", 25:"z"}

# all of the operational code for day 4
def main():
    # each room's information and inverse letterMap
    rooms, invLetters = [], {v: k for k, v in letterMap.items()}

    # read in the information
    with open("info/day4info.txt", 'r') as f:
        # iterate through each line, and format before inserting
        for line in f:
            # split off the sector ID and checksum
            l = line.rsplit("-", 1)
            # split between the checksum and ID
            temp = l[1].split("[")
            temp[1] = temp[1].replace("]", "")
            l[1] = temp[0]
            l.append(temp[1])
            # put the final room information into the greater room list
            rooms.append(l)

    # iterate through all of the rooms and add the sector sums of the real ones
    sectorSum = 0
    for room in rooms:
        # pull out the room name
        encName = room[0]
        # strip hyphens out of it
        encName = encName.replace("-", "")

        # count the letters in the word
        letterCounts = {}
        for letter in encName:
            # check if the letter has been counted yet
            if letter in letterCounts.keys():
                letterCounts[letter] = letterCounts[letter] + 1
            else:
                letterCounts[letter] = 1
            
        # secondary sort them by letters
        sLetters = sorted(letterCounts.items(), key=operator.itemgetter(0))
        # primary sort them by amounts
        sLetters = sorted(sLetters, key=operator.itemgetter(1), reverse=True)
        # slice list to get primary values
        sLetters = sLetters[:5]

        # compile it into a string
        right = True
        for i in range(5):
            if sLetters[i][0] != room[2][i]:
                right = False

        # check if the given checksum is correct
        if right:
            sectorSum += int(room[1])

        # PART 2
        # necessary variables
        origName, shamt = room[0], int(room[1])
        # format the original name
        origName = origName.replace("-", "")

        # container for final string
        finVal = ''
        for letter in origName:
            # get the original value of the letter
            num = invLetters[letter]
            # shift and fetch new letter
            num += shamt
            num = num % 26
            nLetter = letterMap[num]
            # add the new number onto the finVal
            finVal = ''.join([finVal, nLetter])
        
        # print the result into a file
        with open('out/day4out.txt', 'a') as f:
            toWrite = finVal + " at " + room[1] + '\n'
            f.write(toWrite)

    print(sectorSum)

main()