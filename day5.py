"""
Day 5 of Advent of Code
Mohamed Lansari

input: uqwqemis
"""
import hashlib

# all the primary actual code executes here
def main():
    # create the necessary variables
    i, info, currPass = 0, "uqwqemis", ""
    pass2 = ['' for i in range(8)]

    # iterate through the info until we get eight characters in the currPass
    while True:
        # Create a hash with the current index
        key = info + str(i)
        h = hashlib.md5(key.encode('UTF-8')).hexdigest()
        
        # move onto next iteration if it's not viable'
        if h.startswith("00000"):
            print("viable")
            if len(currPass) < 8:
                currPass += h[5]

            # now check for part two viability
            if not '' in pass2:
                break

            if ord(h[5]) >= ord('0') and ord(h[5]) < ord('8'):
                if pass2[int(h[5])] is '':
                    pass2[int(h[5])] = h[6]

        i += 1
    print(currPass, "done")
    print(pass2, "part 2")


main()