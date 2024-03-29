from Services.DatabaseServices.databaseCommands import databaseCommands
from Services.Models.GameSquare import GameSquare


class Clue:

    def __init__(self, gameID, playerName, guideName, clueText, relatedGameSquareList, color="B", numOfWordsHinted=0,
                 badness=-1, numOfWordsCorrectlyGuessed=0, clueID=0):

        self.gameID = gameID
        self.clueText = clueText
        self.guideName = guideName
        self.playerName = playerName
        self.relatedGameSquares = relatedGameSquareList
        self.badness = badness
        self.color = color
        self.numOfWordsHinted = numOfWordsHinted
        self.numOfWordsCorrectlyGuessed = numOfWordsCorrectlyGuessed

        if not clueID:
            self.clueID = databaseCommands.create_clue(self.gameID, self.guideName, self.playerName, self.clueText,
                                                   self.relatedGameSquares,self.numOfWordsHinted, self.color,
                                                    self.badness, self.numOfWordsCorrectlyGuessed)

        else:
            self.clueID = clueID



    def getRelatedGameSquares(self):
        return self.relatedGameSquares

    def updateClue(self, gameSquaresGuessed, badness, numCorrectlyGuessed):
        databaseCommands.update_clue(self.clueID, gameSquaresGuessed, badness, numCorrectlyGuessed)
        return True

    def serialiseClue(self):
        gameData = {
            'GameID': self.gameID,
            'clueText': self.clueText,
            'colour': self.color,
            'numOfHintedWords': self.numOfWordsHinted,
            'playerName': self.playerName,
            'guideName': self.guideName,
            'clueID': self.clueID,
            'badness': -1
        }
        return gameData
