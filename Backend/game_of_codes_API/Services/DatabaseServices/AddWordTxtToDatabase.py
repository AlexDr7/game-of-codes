import wikipedia

from pathlib import Path

from django.db import Error
from Services.DatabaseServices.databaseCommands import databaseCommands



def initializeWordDatabase():
    database = "..\..\GameOfCodesDB"
    # create a database connection

    p = Path(__file__).parents[2]

    filepath = p / 'word-nounlist.txt'

    print(filepath)

    with open(str(filepath)) as fp:
        line = fp.readline()
        while line:
            target_word = line.strip().upper()
            print(target_word)
            searchOutcome = wikipedia.search(target_word)
            if len(searchOutcome):
                print(searchOutcome[0])

                row = databaseCommands.select_word(target_word)
                if row is None:
                    word_id = databaseCommands.create_word(target_word)


            line = fp.readline()

        #word = ('ZOO', 0)
        #word_id = create_word(conn, word)

