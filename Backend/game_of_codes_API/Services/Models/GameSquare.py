from Services.DatabaseServices.sqlCommands import sqlCommands

class GameSquare:

    def __init__(self, color, gameID, word_text="word"):
        self.color = color
        self.gameID = gameID
        if word_text == "word":
            self.wordText = self.getRandomWord()
        else:
            self.wordText = word_text


    def getRandomWord(self):
        conn = sqlCommands.create_connection()
        with conn:
            row = sqlCommands.getRandomWord()

        return row

    def getWord(self):
        return self.word

    def setWord(self, word):
        self.word = word

    def setColor(self, new_color):
        self.color = new_color

    def getColor(self):
        return self.color
