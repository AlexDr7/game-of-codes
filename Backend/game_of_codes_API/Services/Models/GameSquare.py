from Services.DatabaseServices.databaseCommands import databaseCommands

class GameSquare:

    def __init__(self, color, gameID, word_text="word", alreadyExists = True):
        self.color = color
        self.gameID = gameID
        self.isGuessed = False

        if not alreadyExists:
            self.wordText = word_text
            self.squareID = databaseCommands.create_game_square(self.wordText, self.gameID, self.color, self.isGuessed)
        else:
            self.squareID = databaseCommands.select_game_square_gameId_word(self.gameID, word_text).id
            self.wordText = word_text


    def getRandomWord(self):
        return databaseCommands.select_random_word().word_text

    def getWord(self):
        return self.wordText

    def setWord(self, word):
        self.wordText = word

    def setColor(self, new_color):
        self.color = new_color

    def getColor(self):
        return self.color

    def getGameSquareID(self):
        return self.squareID

    def serialiseGameSquare(self, i):
        data = {
            'id': self.squareID,
            'index': i,
            'value': self.wordText,
            'colour': self.color
        }
        return data
