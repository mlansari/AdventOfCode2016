"""
Day 7 of Advent of Code
Mohamed Lansari
"""

# all of the primary execution code
def main():
    ips = []        # ip container

    # read in the ips
    with open("info/day7info.txt", 'r') as f:
        for line in f:
            line = line.strip()
            ips.append(cullHyper(line))

    # iterate through ips and check whether whether it supports TLS
    legitIps = 0
    for ip in ips:
        legit = False
        for ci in range(len(ip)):
            # what to do if it's a hypernet i.e. % 2
            if ci % 2 == 1 and abbaCheck(ip[ci]):
                legit = False
                break   # breka out of the loop for this ip
            elif ci % 2 == 0 and abbaCheck(ip[ci]):
                legit = True

        if legit:
            legitIps += 1
    # print result
    print("TLS Capable IPs: ", legitIps)

    # now check whether it supports SSL
    sslLegits = 0
    for ip in ips:
        # iterate through each ip
        non, hnet = [], []
        for ci in range(len(ip)):           # first construct a list of non-hypernet addresses
            if ci % 2 == 0:
                non.append(ip[ci])
            else:
                hnet.append(ip[ci])
        
        # now check each of those for abas
        if abaCheck(non, hnet):
            sslLegits += 1

    print("SSL Capable IPs: ", sslLegits)

# this method culls out hypernet sequences
def cullHyper(s):
    s = str(s)      # sanitize s
    out = []        # container for outputs
    # run while there are still hypernet addresses
    while '[' in s:
        r = s.split('[', maxsplit=1)
        out.append(r[0])
        r = r[1].split(']', maxsplit=1)
        out.append(r[0])
        if '[' not in r[1]:
            out.append(r[1])

        s = r[1]

    return out

# this method checks if the string contains 'Autonomous Bridge Bypass Notation'
def abbaCheck(s):
    has = False

    # iterate through each character until the fourth to last in the string
    for i in range(len(s) - 3):
        # check whether the next character is different
        if s[i] == s[i + 1]:
            continue
        # check if the one after that is the same as the second
        if s[i + 1] != s[i + 2]:
            continue
        # check if the last is the same as the first
        if s[i] != s[i + 3]:
            continue
        
        has = True
        break

    return has

def abaCheck(superNet, hyperNet):
    for s in superNet:
        for h in hyperNet:
            abas = [a + b + c for a, b, c in zip(s, s[1:], s[2:]) if a == c and a != b]
            checks = [a + b + c for a, b, c in zip(h, h[1:], h[2:]) if a == c and a != b]

            for aba in abas:
                for check in checks:
                    if aba == check[1] + check[0] + check[1]:
                        return True

    return False

main()