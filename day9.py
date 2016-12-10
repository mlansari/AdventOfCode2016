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
    i, length = 0, 0
    while len(com) > 0:
        # split at first close parens
        r = com.split(")", maxsplit=1)
        key = r[0].strip("(")
        key = key.split("x")

        # now we have the key, slice to fetch the string to repeat
        rep = r[1][:int(key[0])]
        length += recursCheckAmnt(rep, int(key[1]))
        for i in range(int(key[1])):
            decom = ''.join([decom, rep])
        
        com = r[1][int(key[0]):]

    print("The length of the decompressed file is", len(decom), "in version 1")
    print(length)

def recursCheckAmnt(strng, amnt):
    # check if it has another iteration
    if "(" in strng:
        # then split and recurse
        r = strng.split("(", maxsplit=1)
        key = r[1].split(")", maxsplit=1)
        print(key)
        new = key[1]
        key = key[0].split("x")
        return amnt * (len(r[0]) + recursCheckAmnt(new, int(key[1])))
    else:
        return amnt * len(strng)

main()