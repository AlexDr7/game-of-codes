from Services.DatabaseServices.databaseCommands import databaseCommands

class GameSquare:

    def __init__(self, color, gameID, word_text="word"):
        self.color = color
        self.gameID = gameID
        if word_text == "word":
            self.wordText = self.getRandomWord()
        else:
            self.wordText = word_text

        self.isGuessed = False

        self.squareID = databaseCommands.create_game_square(self.wordText, self.gameID, self.color, self.isGuessed)



    def getRandomWord(self):
        return databaseCommands.select_random_word().word_text

    def getWord(self):
        return self.word

    def setWord(self, word):
        self.word = word

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
