from django.db import Error
from Services.models import Word, Game, Game_Square, Clue, Agent

from random import randint

class databaseCommands:
    database = "GameOfCodesDB"

    def create_word(word):
        w = Word(word_text=word)
        w.save()
        return w.word_text

    def select_word(word):
        try:
            w = Word.objects.get(word_text=word)
        except Word.DoesNotExist:
            return None
        return w

    def select_random_word():
        count = Word.objects.count()
        if count == 0:
            return None
        random_index = randint(0, count - 1)
        w = Word.objects.all()[random_index]
        return w

    def delete_word(word):
        w = Word.objects.get(word_text=word)
        w.delete()
        return True


    def create_game(bluePlayer = "HumanP", blueGuide= "HumanG", redPlayer = "HumanP", redGuide = "HumanG",
                    numOfBlueWords = 9, numOfRedWords = 8, isCompleted= False, blueCorrectGuesses=0,
                    blueWrongGuesses=0, redCorrectGuesses=0, redWrongGuesses=0,
                    isSingleMode = False, isBlueFirst = True):

        g = Game(is_completed=isCompleted, blue_player_id=bluePlayer, red_player_id=redPlayer, blue_guide_id=blueGuide
                 , red_guide_id=redGuide, blue_wrong_guesses=blueWrongGuesses, blue_correct_guesses=blueCorrectGuesses,
                 red_wrong_guesses=redWrongGuesses, red_correct_guesses=redCorrectGuesses, is_blue_first=isBlueFirst
                 , is_single_mode=isSingleMode, num_of_blue_words=numOfBlueWords, num_of_red_words=numOfRedWords)
        g.save()



        return g.id

    def select_game(gameID):
        g = Game.objects.get(pk=gameID)
        return g

    def update_game_isCompleted(gameID, isCompleted, blueCorrectGuesses, blueWrongGuesses, redCorrectGuesses,
                                redWrongGuesses, winner):

        g = Game.objects.get(pk=gameID)
        g.is_completed = isCompleted
        g.blue_correct_guesses = blueCorrectGuesses
        g.blue_wrong_guesses = blueWrongGuesses
        g.red_correct_guesses = redCorrectGuesses
        g.red_wrong_guesses = redWrongGuesses
        g.winner = winner
        g.save()

        if not g.is_single_mode:

            if winner == "B":
                winning_player = databaseCommands.addWinToAgent(g.blue_player)
                winning_guide = databaseCommands.addWinToAgent(g.blue_guide)

                losing_player = databaseCommands.addLoseToAgent(g.red_player)
                losing_guide = databaseCommands.addLoseToAgent(g.red_guide)

            elif winner == "R":
                winning_player = databaseCommands.addWinToAgent(g.red_player)
                winning_guide = databaseCommands.addWinToAgent(g.red_guide)

                losing_player = databaseCommands.addLoseToAgent(g.blue_player)
                losing_guide = databaseCommands.addLoseToAgent(g.blue_guide)
        else:
            if winner == "B":
                winning_player = databaseCommands.addSingleWinToAgent(g.blue_player)
                winning_guide = databaseCommands.addSingleWinToAgent(g.blue_guide)

            elif winner == "R":
                losing_player = databaseCommands.addSingleLoseToAgent(g.blue_player)
                losing_guide = databaseCommands.addSingleLoseToAgent(g.blue_guide)

        return g.id

    def addWinToAgent(agentID):
        ag = databaseCommands.select_agent(agentID)
        ag.num_of_wins = ag.num_of_wins + 1
        ag.total_games = ag.total_games + 1
        ag.save()

    def addSingleWinToAgent(agentID):
        ag = databaseCommands.select_agent(agentID)
        ag.num_of_single_wins = ag.num_of_single_wins + 1
        ag.total_single_games = ag.total_single_games + 1
        ag.save()

    def addLoseToAgent(agentID):
        ag = databaseCommands.select_agent(agentID)
        ag.num_of_losses = ag.num_of_losses + 1
        ag.total_games = ag.total_games + 1
        ag.save()

    def addSingleLoseToAgent(agentID):
        ag = databaseCommands.select_agent(agentID)
        ag.num_of_single_losses = ag.num_of_single_losses + 1
        ag.total_single_games = ag.total_single_games + 1
        ag.save()

    def delete_game(gameID):
        g = Game.objects.get(pk=gameID)
        g.delete()


    def create_game_square(word, game, color, isGuessed):
        g = databaseCommands.select_game(game)
        gs = Game_Square(word_id=word,game=g,color=color,is_guessed=isGuessed)
        gs.save()
        return gs.id

    def update_game_square(squareID, isGuessed):

        gs = Game_Square.objects.get(pk=squareID)
        gs.is_guessed = isGuessed
        gs.save()

        return gs.id

    def select_game_square(squareID):
        gs = Game_Square.objects.get(pk=squareID)
        return gs

    def select_game_square_gameId_word(gameID, word):
        gs = Game_Square.objects.filter(game_id=gameID, word=word)
        if len(gs)>1:
            print(" ERROR select_game_square_gameId_word returned MORE THAN 2 ITEMS gameId:" + str(gameID)+ " word:"+word)
            for sqr in gs:
                print("Square ID:" + str(sqr.id))

        return gs[0]

    def select_game_squares_based_on_game(gameID):
        return Game_Square.objects.filter(game_id=gameID)

    def delete_game_square(squareID):
        gs = Game_Square.objects.get(pk=squareID)
        gs.delete()

    def create_clue(gameID, agentGuideID, agentPlayerID, clueText, wordlistHinted, numWordsHinted=0, colour="B",
                    badness=-1, numWordsCorrectlyGuessed=0):

        g = databaseCommands.select_game(gameID)
        agP = databaseCommands.select_agent(agentPlayerID)
        agG = databaseCommands.select_agent(agentGuideID)
        c = Clue(game=g, agent_guide=agG, agent_player=agP, badness=badness, clue_text=clueText, color=colour,
                 num_of_words_hinted=numWordsHinted, num_of_words_correctly_guessed=numWordsCorrectlyGuessed)
        c.save()
        for word in wordlistHinted:
            if isinstance(word,str):
                sq = databaseCommands.select_game_square_gameId_word(gameID, word)
                c.words_hinted.add(sq)

        c.save()
        return c.id

    def select_clue(clueID):
        c = Clue.objects.get(pk=clueID)
        return c

    def select_clue_gameId_clueText(gameId, clueText):
        c = Clue.objects.filter(game_id=gameId, clue_text=clueText)
        if len(c) == 0 :
            return None
        return c[0]

    def update_clue(clueID, wordlistGuessed, badness, numWordsCorrectlyGuessed):
        c = Clue.objects.get(pk=clueID)
        c.badness = badness
        c.num_of_words_correctly_guessed = numWordsCorrectlyGuessed

        for word in wordlistGuessed:
            if isinstance(word,str):
                sq = databaseCommands.select_game_square_gameId_word(c.game.id, word)
                c.words_hinted.add(sq)

        c.save()
        return c.id

    def select_agent(agentID):
        ag = Agent.objects.get(pk=agentID)
        return ag
