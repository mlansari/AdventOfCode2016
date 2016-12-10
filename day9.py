"""
Day 9 of Advent of Code
Mohamed Lansari
 """

# main code goes here
def main():
    com, decom = "", ""

    with open('info/day9info.txt', 'r') as f:
        com = f.read()

    # iterate through compressed
    i, length, v1length = 0, 0, 0
    while len(com) > 0:
        # split at the first open parentheses
        r = com.split("(", maxsplit=1)
        # check whether or not there actually were any more parens
        if len(r) > 1:
            key = r[1].split(")", maxsplit=1)
            text = key[1]
            info = key[0].split("x")
            # join median text
            length += len(r[0])             # increase the length by the amount prior to the recursion
            decom = ''.join([decom, r[0]])
            v1length += len(r[0])

            # with the key, recursively fetch the string to repeat it
            slc = text[:int(info[0])]
            length += recursCheckAmnt(slc, int(info[1]))
            for i in range(int(info[1])):
                decom = ''.join([decom, slc])
                v1length += len(slc)

            com = text[int(info[0]):] 
        else:
            decom = ''.join([decom, com])
            v1length += len(com)
            length += len(com)
            com = ""

    print("The length of the decompressed file is", v1length, "in version 1")
    print("The length of the decompressed file is", length, "in version 2")

# after much struggle, this worked properly for part 2
def recursCheckAmnt(strng, amnt):
    with open('out/day9out.txt', 'a') as f:
        f.write("Checking " + strng + " with iterations of " + str(amnt) + "\n")
    # check if it has another iteration
    rAmount = 0
    while len(strng) > 0:
        if "(" in strng:
            # then split and recurse
            r = strng.split("(", maxsplit=1)
            key = r[1].split(")", maxsplit=1)
            new = key[1]                        # this is the new text
            key = key[0].split("x")

            passamnt = new[:int(key[0])]
            restamnt = new[int(key[0]):]

            rAmount += (len(r[0]) + recursCheckAmnt(passamnt, int(key[1])))
            strng = restamnt
        else:
            rAmount += len(strng)
            strng = ""
    
    with open('out/day9out.txt', 'a') as f:
        f.write("Returning with a value of " + str(amnt * rAmount) + '\n')
    return amnt * rAmount

main()