from Services.Models.Game import Game
from Services.Models.Clue import Clue

class JSONParser:

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

        gameID = json["gameID"]
        clueText = json["clueText"]

        numOfRelated = json["numOfHintedWords"]
        color = json["colour"]

        agentPlayer = json["playerName"]
        agentGuide = json["guideName"]

        relatedGameSquares = list()

        return Clue(gameID, agentPlayer, agentGuide, clueText, relatedGameSquares, color, numOfRelated)
