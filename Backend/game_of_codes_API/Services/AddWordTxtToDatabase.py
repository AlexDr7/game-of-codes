import sqlite3
import wikipedia

from django.db import Error


def main():
    database = "..\GameOfCodesDB"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project

        filepath = '..\word-nounlist.txt'
        with open(filepath) as fp:
            line = fp.readline()
            while line:
                target_word = line.strip().upper()
                print(target_word)
                searchOutcome = wikipedia.search(target_word)
                if len(searchOutcome):
                    print(searchOutcome[0])

                    row = select_word(conn, target_word)
                    if len(row) == 0:
                        word_id = create_word(conn, target_word)


                line = fp.readline()


        #word = ('ZOO', 0)
        #word_id = create_word(conn, word)

def create_connection(db_file):
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
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO Services_word(word_text)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute("INSERT INTO Services_word(word_text) VALUES(?)", (word,))
    return cur.lastrowid

def select_word(conn, word):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = 'SELECT * FROM Services_word WHERE word_text=?'
    cur = conn.cursor()
    cur.execute(sql, (word,))

    rows = cur.fetchall()
    return rows

if __name__ == '__main__':
    main()

