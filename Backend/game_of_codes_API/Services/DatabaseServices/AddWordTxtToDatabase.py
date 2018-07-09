import sqlite3
import wikipedia

from django.db import Error
from Services.DatabaseServices.sqlCommands import sqlCommands


def main():
    database = "..\GameOfCodesDB"

    # create a database connection
    conn = sqlCommands.create_connection(database)
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

                    row = sqlCommands.select_word(conn, target_word)
                    if len(row) == 0:
                        word_id = sqlCommands.create_word(conn, target_word)


                line = fp.readline()


        #word = ('ZOO', 0)
        #word_id = create_word(conn, word)


if __name__ == '__main__':
    main()

