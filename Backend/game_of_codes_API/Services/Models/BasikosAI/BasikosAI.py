import math

from Services.DatabaseServices.databaseCommands import databaseCommands
from Services.Models.BasikosAI.TantalusWordAssociation import TantalusWordAssociation
from Services.Models.Clue import Clue
from Services.Models.BasikosAI.WordAssociation import WordAssociation
from Services.Models.BasikosAI.ErmisWordAssociation import ErmisWordAssociation

class BasikosAI:

    def __init__(self, board, turn):
        self.gameID = board.gameID
        self.board = board
        self.team = turn

        gameDatabaseObject = databaseCommands.select_game(self.gameID)

        if turn == "B":
            self.player = gameDatabaseObject.blue_player_id
            self.guide = gameDatabaseObject.blue_guide_id
        else:
            self.player = gameDatabaseObject.red_player_id
            self.guide = gameDatabaseObject.red_guide_id

        self.wordAssoc = WordAssociation(self.board)

    def ErmisRelateWordsGetClue(self):
        self.wordAssoc = ErmisWordAssociation(self.board, 2000, 10)

        if self.team == "B":
            numberOfWords = len(self.board.blueWords)
            numOfArticlesToCheck = math.floor(9 / numberOfWords)
            if numberOfWords < 8:
                numOfArticlesToCheck = numOfArticlesToCheck + 2

            print(numOfArticlesToCheck, " this many artcles are checked")
            self.wordAssoc.calculateSimpleRelevantWords(self.board.blueWords, numOfArticlesToCheck)
            print("Number of relevant " + str(self.wordAssoc.commonWordsLength()))

            if numOfArticlesToCheck > 3:
                print(" check red")
                self.wordAssoc.deleteEveryWordAssociatedWith(self.board.redWords, 1)
                print("Number of relevant after deletion of opponent words " + str(self.wordAssoc.commonWordsLength()))

        else:
            numberOfWords = len(self.board.redWords)

            numOfArticlesToCheck = math.floor(9 / numberOfWords)
            if numberOfWords < 8:
                numOfArticlesToCheck = numOfArticlesToCheck + 2

            self.wordAssoc.calculateSimpleRelevantWords(self.board.redWords, numOfArticlesToCheck)
            print("Number of relevant " + str(self.wordAssoc.commonWordsLength()))

            if numOfArticlesToCheck > 3:
                self.wordAssoc.deleteEveryWordAssociatedWith(self.board.blueWords, 1)
                print("Number of relevant after deletion of opponent words " + str(self.wordAssoc.commonWordsLength()))

        self.wordAssoc.deleteCommonWordsThatAppearInEveryWord()
        print("Number of relevant after deletion of words that appear a lot " + str(self.wordAssoc.commonWordsLength()))

        self.wordAssoc.deleteEveryWordAssociatedWith(self.board.purpleWord, 3)
        print("Number of relevant after deletion of purple words " + str(self.wordAssoc.commonWordsLength()))

        clue = self.wordAssoc.getBestClue(numberOfWords)

        if numberOfWords > 1:
            clues = self.wordAssoc.getSortedListOfCommonWords()
        else:
            clues = self.wordAssoc.getSortedListOfAllWords()

        i = 0
        if len(clues) > 1:
            while databaseCommands.select_clue_gameId_clueText(self.gameID, clues[i][0]) is not None:
                i += 1

            clue = clues[i]

        else:
            clue = clues
        print(clue)

        clueObject = Clue(self.gameID, self.player, self.guide, clue[0], clue[1], self.team, len(clue[1]) - 1)

        return clueObject

    def VasikiaRelateWordsGetClue(self):

        if self.team == "B":
            numberOfWords = len(self.board.blueWords)
            self.wordAssoc.calculateSimpleRelevantWords(self.board.blueWords, 2)
            print("Number of relevant " + str(self.wordAssoc.commonWordsLength()))

            self.wordAssoc.deleteEveryWordAssociatedWith(self.board.redWords, 1)
            print("Number of relevant after deletion of opponent words " + str(self.wordAssoc.commonWordsLength()))

        else:
            numberOfWords = len(self.board.redWords)
            self.wordAssoc.calculateSimpleRelevantWords(self.board.redWords, 2)
            print("Number of relevant " + str(self.wordAssoc.commonWordsLength()))

            self.wordAssoc.deleteEveryWordAssociatedWith(self.board.blueWords, 1)
            print("Number of relevant after deletion of opponent words " + str(self.wordAssoc.commonWordsLength()))


        self.wordAssoc.deleteCommonWordsThatAppearInEveryWord()
        print("Number of relevant after deletion of words that appear a lot " + str(self.wordAssoc.commonWordsLength()))

        self.wordAssoc.deleteEveryWordAssociatedWith(self.board.purpleWord, 3)
        print("Number of relevant after deletion of purple words " + str(self.wordAssoc.commonWordsLength()))

        clue = self.wordAssoc.getBestClue(numberOfWords)

        if numberOfWords > 1:
            clues = self.wordAssoc.getSortedListOfCommonWords()
        else:
            clues = self.wordAssoc.getSortedListOfAllWords()

        i = 0
        if len(clues) > 1:
            while databaseCommands.select_clue_gameId_clueText(self.gameID,clues[i][0]) is not None:
                i += 1

            clue = clues[i]

        else:
            clue = clues
        print(clue)

        clueObject = Clue(self.gameID, self.player, self.guide, clue[0], clue[1], self.team, len(clue[1])-1)

        return clueObject

    def TantalusRelateWordsGetClue(self):

        if self.team == "B":
            numberOfWords = len(self.board.blueWords)
            self.wordAssoc.calculateSimpleRelevantWords(self.board.blueWords, 2)
            print("Number of relevant " + str(self.wordAssoc.commonWordsLength()))

        else:
            numberOfWords = len(self.board.redWords)
            self.wordAssoc.calculateSimpleRelevantWords(self.board.redWords, 2)
            print("Number of relevant " + str(self.wordAssoc.commonWordsLength()))

        self.wordAssoc.deleteCommonWordsThatAppearInEveryWord()
        print("Number of relevant after deletion of words that appear a lot " + str(self.wordAssoc.commonWordsLength()))

        self.wordAssoc.deleteEveryWordAssociatedWith(self.board.purpleWord, 2)
        print("Number of relevant after deletion of purple words " + str(self.wordAssoc.commonWordsLength()))

        clue = self.wordAssoc.getBestClue(numberOfWords)

        if numberOfWords > 1:
            clues = self.wordAssoc.getSortedListOfCommonWords()
        else:
            clues = self.wordAssoc.getSortedListOfAllWords()

        i = 0
        if len(clues) > 1:
            while databaseCommands.select_clue_gameId_clueText(self.gameID,clues[i][0]) is not None:
                i += 1

            cluePercent = clues[i][1][0] - clues[i][1][0] * 0.17
            bestClue = clues[i]
            maxRelatedWordsToClue = len(clues[i][1]) - 1

            while clues[i][1][0] > cluePercent and i < len(clues) - 1:
                if len(clues[i][1]) - 1 > maxRelatedWordsToClue and databaseCommands.select_clue_gameId_clueText(self.gameID,clues[i][0]) is not None:
                    bestClue = clues[i]
                i += 1

            clue = bestClue

        else:
            clue = clues

        print(clue)
        clueObject = Clue(self.gameID, self.player, self.guide, clue[0], clue[1], self.team, len(clue[1])-1)

        return clueObject

    def VasikiaRelateClueGetWords(self, clue):
        words = list()

        self.wordAssoc.relateClueToWordsOnBoardforPlayer(clue.clueText, self.board.activeWordsOnBoard, 5, 2, 1500)

        relatedWords = self.wordAssoc.getSortedListOfCommonWordsForPlayer()
        print(relatedWords)
        for i in range(0, int(clue.numOfWordsHinted)):
            words.append(relatedWords[i][1][1])


        print(words)

        return words

    def ErmisRelateClueGetWords(self, clue):
        words = list()

        self.wordAssoc = ErmisWordAssociation(self.board, 2000, 10)

        numberOfArticlesToCheck = math.floor(25/len(self.board.activeWordsOnBoard))

        if len(self.board.activeWordsOnBoard) <= 5:
            numberOfArticlesToCheck -= 2

        self.wordAssoc.relateClueToWordsOnBoardforErmisPlayer(clue.clueText, self.board.activeWordsOnBoard, 6, numberOfArticlesToCheck)

        relatedWords = self.wordAssoc.getSortedListOfCommonWordsForPlayer()
        print(relatedWords)
        for i in range(0, int(clue.numOfWordsHinted)):
            words.append(relatedWords[i][1][1])

        print(words)

        return words

    def TantalusRelateClueGetWords(self, clue):
        words = list()

        self.wordAssoc = TantalusWordAssociation(self.board, 2000, 10)

        self.wordAssoc.TantalusRelateClueToWordsOnBoardforPlayer(clue.clueText, self.board.activeWordsOnBoard, 10, 2)

        relatedWords = self.wordAssoc.getSortedListOfCommonWordsForPlayer()
        print(relatedWords)
        for i in range(0, int(clue.numOfWordsHinted)):
            words.append(relatedWords[i][1][1])

        print(words)

        return words


