from Services.DatabaseServices.sqlCommands import sqlCommands

class GameSquare:

    def __init__(self, color, gameID, word_text="word"):
        self.color = color
        self.gameID = gameID
        if word_text == "word":
            self.wordText = self.getRandomWord()
        else:
            self.wordText = word_text

        self.isGuessed = False

        conn = sqlCommands.create_connection()
        with conn:
            self.squareID = sqlCommands.create_game_square(conn, self.wordText, self.gameID, self.color, self.isGuessed)

        conn.commit()
        conn.close()


    def getRandomWord(self):
        conn = sqlCommands.create_connection()
        with conn:
            row = sqlCommands.getRandomWord()

        conn.commit()
        conn.close()

        return row

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

    def serialiseGameSquare(self):
        data = {
            'id': self.squareID,
            'value': self.wordText,
            'colour': self.color
        }
        return data
