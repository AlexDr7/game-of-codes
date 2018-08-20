from Services.Models.Game import Game
from Services.Models.Clue import Clue
from Services.Models.WordBoard import WordBoard

from Services.DatabaseServices.databaseCommands import databaseCommands

class JSONParser:

    def deserialiseBoard(json):
        gameid = json["GameID"]
        game = databaseCommands.select_game(gameid)
        numOfBlueWords = game.num_of_blue_words
        numOfRedWords = game.num_of_red_words

        board = WordBoard(gameid,numOfBlueWords,numOfRedWords)

        board.deserialiseBoard()
        return board

    def deserializeGameSettingsAndCreateGame(json):

        singleMode = json["singleMode"]

        blueTeamPlayer = json["bluePlayer"]
        blueTeamGuide = json["blueGuide"]

        if not singleMode:
            redTeamPlayer = json["redPlayer"]
            redTeamGuide = json["redGuide"]
        else:
            redTeamGuide = "null"
            redTeamPlayer = "null"
            return Game(blueTeamPlayer, redTeamPlayer, blueTeamGuide, redTeamGuide, singleMode, 9, 8)

        return Game(blueTeamPlayer, redTeamPlayer, blueTeamGuide, redTeamGuide, singleMode)

    def deserializeClueAndCreateClue(json):

        gameID = json["GameID"]
        clueText = json["clueText"]

        numOfRelated = json["numOfHintedWords"]
        color = json["colour"]

        agentPlayer = json["playerName"]
        agentGuide = json["guideName"]

        relatedGameSquares = list()

        return Clue(gameID, agentPlayer, agentGuide, clueText, relatedGameSquares, color, numOfRelated)

    def deserializeClue(json):

        gameID = json["GameID"]
        clueText = json["clueText"]

        numOfRelated = json["numOfHintedWords"]
        color = json["colour"]

        agentPlayer = json["playerName"]
        agentGuide = json["guideName"]

        clueID = json["clueID"]

        relatedGameSquares = list()

        return Clue(gameID, agentPlayer, agentGuide, clueText, relatedGameSquares, color, numOfRelated, -1, 0, clueID)

    def deserializeUpdateClue(json):

        clueID = json["clueID"]
        numWordsCorrectlyGuessed = json["numOfCorrectlyGuessed"]
        badness = json["badness"]

        wordlistGuessed = list()

        for object in json["wordsGuessed"]:
            squareID = object["id"]
            wordlistGuessed.append(squareID)
            databaseCommands.update_game_square(squareID, True)

        return databaseCommands.update_clue(clueID, wordlistGuessed, badness, numWordsCorrectlyGuessed)

    def deserializeUpdateGame(json):

        gameID = json["GameID"]
        isComplete = True

        blueCorrectGuesses = json["blueCorrectGuesses"]
        blueWrongGuesses = json["blueWrongGuesses"]
        redCorrectGuesses = json["redCorrectGuesses"]
        redWrongGuesses = json["redWrongGuesses"]

        winner = json["winner"]

        return databaseCommands.update_game_isCompleted(gameID, isComplete, blueCorrectGuesses, blueWrongGuesses,
                                                        redCorrectGuesses, redWrongGuesses, winner)