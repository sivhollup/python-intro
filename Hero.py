class Hero(object):

    def __init__(self, position, maxStr):
        self.position = position
        self.maxStr = maxStr

    def moveRight(self, length):
        if not self.position[0] + length > self.maxStr:
            self.position = self.position[0] + length, self.position[1]
            print("New position: %d, %d" %(self.position))
            self.printPosition()
        else:
            print("Would go off the board, position: %d, %d" % (self.position))

    def printPosition(self):
        self.printXLine()
        for x in range(0, self.maxStr):
            oneLine = ""
            for y in range(0, self.maxStr):
                if self.position == (y, x):
                    oneLine += "| * "
                else:
                    oneLine += "|   "
            oneLine += "|"
            print(oneLine)
            self.printXLine()
            

    def printXLine(self):
        oneLine = ""
        for i in range(0, self.maxStr):
            oneLine += "+---"
        oneLine += "+"
        print(oneLine)
