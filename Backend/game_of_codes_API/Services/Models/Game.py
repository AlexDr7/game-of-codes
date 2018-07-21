import random

from Services.DatabaseServices.databaseCommands import databaseCommands
from Services.Models.WordBoard import WordBoard


class Game:

    def __init__(self, blueTeamPlayer = "HumanP", redTeamPlayer = "HumanP", blueTeamGuide = "HumanG",
                 redTeamGuide = "HumanG", isSingleMode=False, numOfBlueWords=0, numOfRedWords=0):

        if numOfBlueWords != 0:
            self.numOfBlueWords = numOfBlueWords
            self.numOfRedWords = numOfRedWords
            self.isBluesFirst = True
        else:
            whoFirst = random.randint(0, 1)
            if whoFirst == 0:
                self.numOfBlueWords = 9
                self.numOfRedWords = 8
                self.isBluesFirst = True
            else:
                self.numOfBlueWords = 8
                self.numOfRedWords = 9
                self.isBluesFirst = False

        self.isGameCompleted = False
        self.isSingleMode = isSingleMode

        self.bluePlayer = blueTeamPlayer
        self.blueGuide = blueTeamGuide
        self.redPlayer = redTeamPlayer
        self.redGuide = redTeamGuide

        self.blueCorrectGuesses = 0
        self.blueWrongGuesses = 0
        self.redCorrectGuesses = 0
        self.redWrongGuesses = 0

        self.gameID = databaseCommands.create_game(self.bluePlayer, self.blueGuide, self.redPlayer, self.redGuide,
                                                   self.numOfBlueWords, self.numOfRedWords, self.isGameCompleted,
                                                   self.blueCorrectGuesses, self.blueWrongGuesses,
                                  self.redCorrectGuesses, self.redWrongGuesses, self.isSingleMode, self.isBluesFirst)

        self.board = WordBoard(self.gameID, self.numOfBlueWords, self.numOfRedWords)
        self.board.fillBoardWithRandomWords(self.gameID)



    def serialiseGame(self):
        gameData = {
            'GameID': self.gameID,
            'isBlueFirst': self.isBluesFirst,
            'blueWordsCount': self.numOfBlueWords,
            'redWordsCount': self. numOfRedWords
        }
        gameData = self.board.serialiseBoard(gameData)
        return gameData