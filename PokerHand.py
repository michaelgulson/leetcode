class PokerHand:
    def __init__(self, pokerCards):
        self.suits = {}
        self.numbers = {}
        for pokerCard in pokerCards:
            if(self.numbers.get(pokerCard[0]) == None):
                self.numbers[pokerCard[0]] = 1
            else:
                self.numbers[pokerCard[0]] = self.numbers[pokerCard[0]] +1
            if(self.suits.get(pokerCard[1]) == None):
                self.suits[pokerCard[1]] = 1
            else:
                self.suits[pokerCard[1]] = self.suits[pokerCard[1]] +1  

    def printHand(self):
        print("numbers: ", self.numbers)
        print("suits: ", self.suits)

    def isFlush(self):
        if 5 in self.suits.values():
            return True
        else:
            return False

exampleHand = ["1A", "2A", "2A", "2A", "5A"]
pokerHand = PokerHand(exampleHand)
pokerHand.printHand()
print(pokerHand.isFlush())

