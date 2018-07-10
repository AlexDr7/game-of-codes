import random

from Services.DatabaseServices.sqlCommands import sqlCommands
from Services.Models.WordBoard import WordBoard

class Game:

    def __init__(self, numOfBlueWords=0, numOfRedWords=0, blueTeamPlayer = "HumanP", redTeamPlayer = "HumanP",
                 blueTeamGuide = "HumanG", redTeamGuide = "HumanG"):
        if numOfBlueWords != 0:
            self.numOfBlueWords = numOfBlueWords
            self.numOfRedWords = numOfRedWords
        else:
            whoFirst = random.randint(0, 1)
            if whoFirst == 0:
                self.numOfBlueWords = 9
                self.numOfRedWords = 8
            else:
                self.numOfBlueWords = 8
                self.numOfRedWords = 9

        self.isGameCompleted = False

        self.bluePlayer = blueTeamPlayer
        self.blueGuide = blueTeamGuide
        self.redPlayer = redTeamPlayer
        self.redGuide = redTeamGuide

        self.blueCorrectGuesses = 0
        self.blueWrongGuesses = 0
        self.redCorrectGuesses = 0
        self.redWrongGuesses = 0

        conn = sqlCommands.create_connection()
        with conn:
            self.gameID = sqlCommands.create_game(conn, self.bluePlayer, self.blueGuide, self.redPlayer, self.redGuide,
                                                  self.isGameCompleted, self.blueCorrectGuesses, self.blueWrongGuesses,
                                                  self.redCorrectGuesses, self.redWrongGuesses)

        conn.commit()
        conn.close()
        self.board = WordBoard(self.gameID, self.numOfBlueWords, self.numOfRedWords)
        self.board.fillBoardByTemplate(1, self.gameID)



    def serialiseGame(self):
        gameData = {
            'GameID': self.gameID,
            'Board': self.board.serialiseBoard()
        }

        return gameData