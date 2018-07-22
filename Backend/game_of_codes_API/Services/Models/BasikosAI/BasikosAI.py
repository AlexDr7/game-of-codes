from Services.DatabaseServices.databaseCommands import databaseCommands
from Services.Models.Clue import Clue
from Services.Models.BasikosAI.WordAssociation import WordAssociation
from Services.Models.WordBoard import WordBoard

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


    def relateWordsgetClue(self):

        if self.team == "B":
            self.wordAssoc.calculateSimpleRelevantWords(self.board.blueWords, 5)
            print("Number of relevant " + str(self.wordAssoc.commonWordsLength()))

            self.wordAssoc.deleteEveryWordAssociatedWith(self.board.redWords, 1)
            print("Number of relevant after deletion of opponent words " + str(self.wordAssoc.commonWordsLength()))

        else:
            self.wordAssoc.calculateSimpleRelevantWords(self.board.redWords, 5)
            print("Number of relevant " + self.wordAssoc.commonWordsLength())

            self.wordAssoc.deleteEveryWordAssociatedWith(self.board.blueWords, 1)
            print("Number of relevant after deletion of opponent words " + str(self.wordAssoc.commonWordsLength()))


        self.wordAssoc.deleteCommonWordsThatAppearInEveryWord()
        print("Number of relevant after deletion of words that appear a lot " + str(self.wordAssoc.commonWordsLength()))

        self.wordAssoc.deleteEveryWordAssociatedWith(self.board.purpleWord, 3)
        print("Number of relevant after deletion of purple words " + str(self.wordAssoc.commonWordsLength()))

        clue = self.wordAssoc.getBestClue()
        clues = self.wordAssoc.getSortedListOfCommonWords()
        i = 0
        while databaseCommands.select_clue_gameId_clueText(self.gameID,clues[i][0]) is not None:
            i+=1

        clue = clues[i]

        clueObject = Clue(self.gameID, self.player, self.guide, clue[0], clue[1], self.team, len(clue[1])-1)

        return clueObject

    def relateClueGetWords(self, clue):
        words = list()

        self.wordAssoc.relateClueToWordsOnBoardforPlayer(clue.clueText, self.board.activeWordsOnBoard, 8, 6, 2000)

        relatedWords = self.wordAssoc.getSortedListOfCommonWordsForPlayer()
        print(relatedWords)
        for i in range(0, int(clue.numOfWordsHinted)):
            words.append(relatedWords[i][1][1])


        print(words)

        return words


