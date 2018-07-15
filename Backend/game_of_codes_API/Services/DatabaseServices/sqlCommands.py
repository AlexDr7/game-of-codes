import sqlite3

from django.db import Error

class sqlCommands:
    database = "..\GameOfCodesDB"

    def create_connection(db_file="GameOfCodesDB"):

        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

        return None

    def create_word(conn, word):
        """
        Create a new word into the words table
        :param conn:
        :param word:
        :return: word id
        """
        sql = ''' INSERT INTO Services_word(word_text)
                  VALUES(?) '''
        cur = conn.cursor()
        cur.execute("INSERT INTO Services_word(word_text) VALUES(?)", (word,))
        return cur.lastrowid

    def create_game(conn, bluePlayer = "HumanP", blueGuide= "HumanG", redPlayer = "HumanP", redGuide = "HumanG",
                isCompleted= False, blueCorrectGuesses=0, blueWrongGuesses=0, redCorrectGuesses=0, redWrongGuesses=0,
                    isSingleMode = False, isBlueFirst = True):
        """
        Create a new word into the words table
        :param conn:
        :param word:
        :return: word id
        """
        sql = ''' INSERT INTO Services_game(is_completed,blue_player_id,red_player_id,blue_guide_id,red_guide_id,
        blue_wrong_guesses,blue_correct_guesses,red_wrong_guesses,red_correct_guesses,
        is_blue_first,is_single_mode)  VALUES(?,?,?,?,?,?,?,?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, (isCompleted, bluePlayer, redPlayer, blueGuide, redGuide, blueWrongGuesses, blueCorrectGuesses,
                          redWrongGuesses, redCorrectGuesses, isBlueFirst, isSingleMode))
        return cur.lastrowid

    def update_game(conn, gameID, isCompleted= False, blueCorrectGuesses=0, blueWrongGuesses=0,
                    redCorrectGuesses=0, redWrongGuesses=0):
        """
        Create a new word into the words table
        :param conn:
        :param word:
        :return: word id
        """
        sql = ''' UPDATE Services_game SET blue_correct_guesses=?, blue_wrong_guesses=?, red_correct_guesses=?,
                  red_wrong_guesses=? WHERE id = ?'''
        cur = conn.cursor()
        cur.execute(sql, (isCompleted, blueCorrectGuesses, blueWrongGuesses, redCorrectGuesses, redWrongGuesses, gameID))

    def create_game_square(conn, word, game, color, isGuessed):
        """
        Create a new word into the words table
        :param conn:
        :param word:
        :return: word id
        """
        sql = ''' INSERT INTO Services_game_square(word_id,game_id,color,is_guessed)  VALUES(?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, (word, game, color, isGuessed))
        return cur.lastrowid

    def update_game_square(conn, squareID, isGuessed):
        """
        Create a new word into the words table
        :param conn:
        :param word:
        :return: word id
        """
        sql = ''' UPDATE Services_game_square SET is_guessed=? WHERE id = ? '''
        cur = conn.cursor()
        cur.execute(sql, (isGuessed, squareID))

    def select_word(conn, word):
        """
        Select a word from the words table
        :param conn:
        :param word:
        :return: row
        """
        sql = 'SELECT * FROM Services_word WHERE word_text=?'
        cur = conn.cursor()
        cur.execute(sql, (word,))

        rows = cur.fetchall()
        return rows

    def getRandomWord(conn):
        """
            Select a random word from the words table
            :param conn:
            :param word:
            :return: row
        """
        sql = 'SELECT * FROM Services_word ORDER BY RANDOM() LIMIT 1'
        cur = conn.cursor()
        cur.execute(sql)

        rows = cur.fetchone()
        return rows[0]

    def create_clue(conn, gameId, colour ="B", wordsHinted=0, wordsCorrectlyGuessed=0):
        """
        Create a new word into the words table
        :param conn:
        :param word:
        :return: word id
        """
        sql = ''' INSERT INTO Services_clue(game,color,num_of_words_hinted,num_of_words_correctly_guessed)  
                  VALUES(?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, (gameId,colour,wordsHinted,wordsCorrectlyGuessed))
        return cur.lastrowid