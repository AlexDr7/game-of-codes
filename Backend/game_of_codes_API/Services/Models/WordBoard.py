import random

from Services.DatabaseServices.databaseCommands import databaseCommands
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

        self.wordsOnBoard = set()
        self.blueWords = []
        self.redWords = []
        self.greyWords = []
        self.purpleWord = []


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
                self.board.append(self.createGameSquareWithRandomWord(colorArr[randColor], gameID))
                numOfPurple += 1
            elif randColor == 1 and numOfBlue < self.numOfBlueWords:
                self.board.append(self.createGameSquareWithRandomWord(colorArr[randColor], gameID))
                numOfBlue += 1
            elif randColor == 2 and numOfRed < self.numOfRedWords:
                self.board.append(self.createGameSquareWithRandomWord(colorArr[randColor], gameID))
                numOfRed += 1
            elif randColor == 3 and numOfGrey < 7:
                self.board.append(self.createGameSquareWithRandomWord(colorArr[randColor], gameID))
                numOfGrey += 1
            else:
                i += -1

            i += 1
        return self.board

    def createGameSquareWithRandomWord(self, color, gameID):
        gs = GameSquare(color, gameID)
        while gs.getWord() in self.wordsOnBoard:
            gs.setWord(gs.getRandomWord())

        self.wordsOnBoard.add(gs.getWord())
        return gs

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

    def deserialiseBoard(self):

        gameSquareList = databaseCommands.select_game_squares_based_on_game(self.gameID)
        for gameSqr in gameSquareList:

            newGameSqr = GameSquare(gameSqr.color, self.gameID, gameSqr.word_id)
            self.board.append(newGameSqr)
            self.wordsOnBoard.add(gameSqr.word_id)
            if not gameSqr.is_guessed:
                if gameSqr.color == "B":
                    self.blueWords.append(gameSqr.word_id)
                elif gameSqr.color == "R":
                    self.redWords.append(gameSqr.word_id)
                elif str(gameSqr.color) == "P":
                    self.purpleWord.append(gameSqr.word_id)
                elif gameSqr.color == "G":
                    self.greyWords.append(gameSqr.word_id)

        return True

