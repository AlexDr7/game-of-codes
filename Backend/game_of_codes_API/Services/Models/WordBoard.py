import random

from Services.Models.GameSquare import GameSquare
from collections import defaultdict

class WordBoard:

    id = 1
    template_words_1 = ["BRIDGE", "KNIFE", "HEART", "VET", "ROCK", "MONSTER", "CAPITAL", "LOCH NESS", "BANK", "CLIFF",
                        "RABBIT", "TRACK", "GLOVE", "BOMB", "CASINO", "LITTER", "SKYSCRAPER", "FAN", "SNOWMAN",
                        "BOTTLE", "TORCH", "LINK",  "BLOCK", "SPRING", "TIE"]
    template_color_1 = ["B", "P", "B", "B", "B", "B", "B", "B", "B", "R", "R", "R", "R", "R", "R", "R", "R", "G", "G"
                        , "G", "G", "G", "G", "G", "G"]

    def __init__(self, gameID, numOfBlueWords=8, numOfRedWords=8):
        self.board = []
        self.numOfBlueWords = numOfBlueWords
        self.numOfRedWords = numOfRedWords
        self.gameID = gameID
        self.size = 25

    def fillBoardWithRandomWords(self, gameID):
        numOfPurple = 0
        numOfBlue = 0
        numOfRed = 0
        numOfGrey = 0
        colorArr = ["P", "B", "R", "G"]

        i = 0

        while i < 25:
            randColor = random.randint(0, 3)
            if randColor == 0 and numOfPurple == 0:
                self.board.append(GameSquare(colorArr[randColor], gameID))
                numOfPurple += 1
            elif randColor == 1 and numOfBlue < self.numOfBlueWords:
                self.board.append(GameSquare(colorArr[randColor], gameID))
                numOfBlue += 1
            elif randColor == 2 and numOfRed < self.numOfRedWords:
                self.board.append(GameSquare(colorArr[randColor], gameID))
                numOfRed += 1
            elif randColor == 3 and numOfGrey < 7:
                self.board.append(GameSquare(colorArr[randColor], gameID))
                numOfGrey += 1
            else:
                i += -1

            i += 1
        return self.board

    def fillBoardByTemplate(self, templateID, gameID):
        for i in range(25):
            self.board.append(GameSquare(WordBoard.template_color_1[i], gameID, WordBoard.template_words_1[i]))

        return self.board

    def getSize(self):
        return self.size

    def getBoard(self):
        return self.board

    def serialiseBoard(self, gameData):
        data = defaultdict(list)

        for i in range(25):
            data["Board"].append(self.board[i].serialiseGameSquare(i))

        gameData.update(data)
        return gameData

