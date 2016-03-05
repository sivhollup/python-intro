class Hero(object):

    def moves(self):
        pass

    def moveRight(self, posisjonX, posisjonY, lengde, boardSize):
        print("Trying to move %d from (%d, %d)" % (lengde, posisjonX, posisjonY))
        if not (posisjonX + lengde) > boardSize:
            posisjonX = (posisjonX + lengde)
        return (posisjonX, posisjonY)


class Hero2(object):

    def __init__(self, boardXLength, boardYLength):
        self.boardXLength = boardXLength
        self.boardYLength = boardYLength


    def moveRight(self, posisjonX, posisjonY, length):
        if not posisjonX + length > self.boardXLength:
            print("Moving from %d, %d, to %d, %d" % (posisjonX, posisjonY,
            posisjonX+length, posisjonY))
            return posisjonX + length, posisjonY
        else:
            print("Couldn't move, would go off the board")


    def moveRight2(self, position, length):
        if not position[0] + length > self.boardXLength:
            print("Moving")
            return (position[0] + length, position[1])


class Hero3(object):

    def __init__(self, position, maxX, maxY):
        self.position = position
        self.maxX = maxX
        self.maxY = maxY

    def moveRight(self, length):
        if not self.position[0] + length > self.maxX:
            self.position = self.position[0] + length, self.position[1]
            print("New position: %d, %d" %(self.position))
            self.printPosition()
        else:
            print("Would go off the board, position: %d, %d" % (self.position))

    def printPosition(self):
        self.printXLine()
        for x in range(0, self.maxX):
            oneLine = ""
            for y in range(0, self.maxY):
                if self.position == (y, x):
                    oneLine += "| * "
                else:
                    oneLine += "|   "
            oneLine += "|"
            print(oneLine)
            self.printXLine()
            

    def printXLine(self):
        oneLine = ""
        for i in range(0, self.maxX):
            oneLine += "+---"
        oneLine += "+"
        print(oneLine)
