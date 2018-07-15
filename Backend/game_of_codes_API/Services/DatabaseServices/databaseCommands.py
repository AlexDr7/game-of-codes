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
                isCompleted= False, blueCorrectGuesses=0, blueWrongGuesses=0, redCorrectGuesses=0, redWrongGuesses=0,
                    isSingleMode = False, isBlueFirst = True):

        g = Game(is_completed=isCompleted, blue_player_id=bluePlayer, red_player_id=redPlayer, blue_guide_id=blueGuide
                 , red_guide_id=redGuide, blue_wrong_guesses=blueWrongGuesses, blue_correct_guesses=blueCorrectGuesses,
                 red_wrong_guesses=redWrongGuesses, red_correct_guesses=redCorrectGuesses, is_blue_first=isBlueFirst
                 , is_single_mode=isSingleMode)
        g.save()

        return g.id

    def select_game(gameID):
        g = Game.objects.get(pk=gameID)
        return g

    def update_game_isCompleted(gameID, isCompleted, blueCorrectGuesses, blueWrongGuesses,redCorrectGuesses,
                                redWrongGuesses):

        g = Game.objects.get(pk=gameID)
        g.is_completed = isCompleted
        g.blue_correct_guesses = blueCorrectGuesses
        g.blue_wrong_guesses = blueWrongGuesses
        g.red_correct_guesses = redCorrectGuesses
        g.red_wrong_guesses = redWrongGuesses
        g.save()

        return g.id

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
        for sq in wordlistHinted:
            c.words_hinted.add(sq)

        c.save()
        return c.id

    def select_clue(clueID):
        c = Game_Square.objects.get(pk=clueID)
        return c

    def update_clue(clueID, wordlistGuessed, badness, numWordsCorrectlyGuessed):
        c = Clue.objects.get(pk=clueID)
        c.badness = badness
        c.num_of_words_correctly_guessed = numWordsCorrectlyGuessed

        for sq2 in wordlistGuessed:
            c.words_guessed.add(sq2)

        c.save()
        return c.id

    def select_agent(agentID):
        ag = Agent.objects.get(pk=agentID)
        return ag
