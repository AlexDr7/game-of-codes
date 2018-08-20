import json

from django.http import HttpResponse
from django.http import Http404
from django.views.decorators.cache import cache_control
from django.views.decorators.csrf import csrf_exempt

from Services.Models.JSONParser import JSONParser
from Services.Models.BasikosAI.BasikosAI import BasikosAI
from Services.DatabaseServices.databaseCommands import databaseCommands
from Services.DatabaseServices.AddWordTxtToDatabase import initializeWordDatabase

@csrf_exempt
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def basikosAI(request):
    response = HttpResponse(content_type="application/json")

    if(request.method == "POST"):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)


        databaseCommands.select_game_squares_based_on_game(3)

    else:
        return HttpResponse("Method not Allowed", status=405)

    return response


@csrf_exempt
def updateClue(request):
    response = HttpResponse(content_type="application/json")
    if (request.method == "POST"):

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        clue = JSONParser.deserializeUpdateClue(body)
        #print(body)
        response = HttpResponse(clue, status=200)

    else:
        return HttpResponse("Method not Allowed", status=405)

    return response

@csrf_exempt
def updateGame(request):
    response = HttpResponse(content_type="application/json")
    if (request.method == "POST"):

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        #print(body)

        game = JSONParser.deserializeUpdateGame(body)

        response = HttpResponse(game, status=200)

    else:
        return HttpResponse("Method not Allowed", status=405)

    return response

@csrf_exempt
def addClue(request):
    response = HttpResponse(content_type="application/json")
    if (request.method == "POST"):

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        print(body)
        clue = JSONParser.deserializeClueAndCreateClue(body)

        response = HttpResponse(clue.clueID, status=201)

    else:
        return HttpResponse("Method not Allowed", status=405)

    return response

@csrf_exempt
def guideVasikiaAskClue(request):

    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body)
        turn = body["teamTurn"]
        board = JSONParser.deserialiseBoard(body)
        agentI = BasikosAI(board, turn)
        clue = agentI.VasikiaRelateWordsGetClue()

        dumpJson = json.dumps(clue.serialiseClue())

        response = HttpResponse(dumpJson, content_type="application/json")

    else:
        return HttpResponse("Method not Allowed", status=405)

    return response

@csrf_exempt
def guideSlowVasikiaAskClue(request):

    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body)
        turn = body["teamTurn"]
        board = JSONParser.deserialiseBoard(body)
        agentI = BasikosAI(board, turn)
        clue = agentI.SlowVasikiaRelateWordsGetClue()

        dumpJson = json.dumps(clue.serialiseClue())

        response = HttpResponse(dumpJson, content_type="application/json")

    else:
        return HttpResponse("Method not Allowed", status=405)

    return response

@csrf_exempt
def guideTantalusAskClue(request):

    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body)
        turn = body["teamTurn"]
        board = JSONParser.deserialiseBoard(body)
        agentI = BasikosAI(board, turn)
        clue = agentI.TantalusRelateWordsGetClue()

        dumpJson = json.dumps(clue.serialiseClue())

        response = HttpResponse(dumpJson, content_type="application/json")

    else:
        return HttpResponse("Method not Allowed", status=405)

    return response

@csrf_exempt
def guideErmisAskClue(request):

    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body)
        turn = body["teamTurn"]
        board = JSONParser.deserialiseBoard(body)
        agentI = BasikosAI(board, turn)
        clue = agentI.ErmisRelateWordsGetClue()

        dumpJson = json.dumps(clue.serialiseClue())

        response = HttpResponse(dumpJson, content_type="application/json")

    else:
        return HttpResponse("Method not Allowed", status=405)

    return response

@csrf_exempt
def playerVasikiaGiveClue(request):

    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body)
        turn = body["teamTurn"]

        board = JSONParser.deserialiseBoard(body)
        agentI = BasikosAI(board, turn)

        clue = JSONParser.deserializeClue(body)

        wordsToBeGuessed = agentI.VasikiaRelateClueGetWords(clue)

        clue.updateClue(wordsToBeGuessed, -1, 0)

        jsonText = {
            'clueID': clue.clueID,
            'wordsToBeGuessed': wordsToBeGuessed
        }

        dumpJson = json.dumps(jsonText)

        response = HttpResponse(dumpJson, content_type="application/json")

    else:
        return HttpResponse("Method not Allowed", status=405)

    return response

@csrf_exempt
def playerSlowVasikiaGiveClue(request):

    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body)
        turn = body["teamTurn"]

        board = JSONParser.deserialiseBoard(body)
        agentI = BasikosAI(board, turn)

        clue = JSONParser.deserializeClue(body)

        wordsToBeGuessed = agentI.SlowVasikiaRelateClueGetWords(clue)

        clue.updateClue(wordsToBeGuessed, -1, 0)

        jsonText = {
            'clueID': clue.clueID,
            'wordsToBeGuessed': wordsToBeGuessed
        }

        dumpJson = json.dumps(jsonText)

        response = HttpResponse(dumpJson, content_type="application/json")

    else:
        return HttpResponse("Method not Allowed", status=405)

    return response

@csrf_exempt
def playerErmisGiveClue(request):

    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body)
        turn = body["teamTurn"]

        board = JSONParser.deserialiseBoard(body)
        agentI = BasikosAI(board, turn)

        clue = JSONParser.deserializeClue(body)

        wordsToBeGuessed = agentI.ErmisRelateClueGetWords(clue)

        clue.updateClue(wordsToBeGuessed, -1, 0)

        jsonText = {
            'clueID': clue.clueID,
            'wordsToBeGuessed': wordsToBeGuessed
        }

        dumpJson = json.dumps(jsonText)

        response = HttpResponse(dumpJson, content_type="application/json")

    else:
        return HttpResponse("Method not Allowed", status=405)

    return response

@csrf_exempt
def playerTantalusGiveClue(request):

    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body)
        turn = body["teamTurn"]

        board = JSONParser.deserialiseBoard(body)
        agentI = BasikosAI(board, turn)

        clue = JSONParser.deserializeClue(body)

        wordsToBeGuessed = agentI.TantalusRelateClueGetWords(clue)

        clue.updateClue(wordsToBeGuessed, -1, 0)

        jsonText = {
            'clueID': clue.clueID,
            'wordsToBeGuessed': wordsToBeGuessed
        }

        dumpJson = json.dumps(jsonText)

        response = HttpResponse(dumpJson, content_type="application/json")

    else:
        return HttpResponse("Method not Allowed", status=405)

    return response

@csrf_exempt
def wordService(request):

    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body)
        game = JSONParser.deserializeGameSettingsAndCreateGame(body)
        dumpJson = json.dumps(game.serialiseGame())

        response = HttpResponse(dumpJson, content_type="application/json")

    else:
        return HttpResponse("Method not Allowed", status=405)

    return response


@csrf_exempt
def initializeDatabase(request):

    if request.method == "POST":

        word = databaseCommands.select_random_word()

        if word is None:
            initializeWordDatabase()
            response = HttpResponse("Success", status=201)
        else:
            response = HttpResponse("Word Database Already Initialised", status=405)


    else:
        return HttpResponse("Method not Allowed", status=405)

    return response