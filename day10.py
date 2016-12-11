"""
Day 10 of Advent of Code
Mohamed Lansari
"""
import collections

class ChipException(Exception):
    pass

class Bot(object):
    def __init__(self, id=None):
        self.id = id
        self.value = None
        self.low = None         # both low and high are other bot objects
        self.high = None

    def setValue(self, value):
        if self.value == None:
            self.value = value
        else:
            high = max(self.value, value)
            low = min(self.value, value)
            if high in (17, 61) and low in (17, 61):
                s = "high: {}, low: {}, in bot: {}".format(high, low, self.id)
                # raise ChipException(s)
            self.high.setValue(high)
            self.low.setValue(low)
            self.value = None

class Bots(object):
    def __init__(self):
        self.values = []
        self.bots = collections.defaultdict(Bot)
        self.outputBins = collections.defaultdict(Bin)
        self.objects = {
            'bot': self.bots,
            'output': self.outputBins
        }

    def getObject(self, type, id):
        id = int(id)            # all ids are integers
        obj = self.objects[type][id]
        if obj.id is None:
            obj.id = id
        return obj

    def setInstruction(self, line):
        p = line.split()
        bot = self.getObject(*p[:2])
        bot.low = self.getObject(*p[5:7])
        bot.high = self.getObject(*p[-2:])

    def readInstructions(self, f):
        for line in f:
            if line.startswith('bot'):
                self.setInstruction(line)
            else:
                self.values.append(line)

    def run(self):
        for item in self.values:
            p = item.split()
            id, value = int(p[-1]), int(p[1])
            self.bots[id].setValue(value)
        print('done')


class Bin(object):
    def __init__(self, id=None):
        self.items = []
        self.id = id

    def setValue(self, value):
        self.items.append(value)


def main():
    bots = Bots()
    with open('info/day10info.txt', 'r') as f:
        bots.readInstructions(f)
    try:
        bots.run()
    except ChipException as err:
        print(err)

    val = bots.outputBins[0].items[0] * bots.outputBins[1].items[0] * bots.outputBins[2].items[0]
    print([bots.outputBins[x].items for x in range(0, 6)])
    print(val)

main()