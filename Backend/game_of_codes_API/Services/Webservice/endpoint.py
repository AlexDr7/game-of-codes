import json

from django.http import HttpResponse
from django.http import Http404
from django.views.decorators.cache import cache_control
from django.views.decorators.csrf import csrf_exempt

from Services.Models.JSONParser import JSONParser
from Services.Models.BasikosAI import BasikosAI
from Services.DatabaseServices.databaseCommands import databaseCommands
from Services.DatabaseServices.AddWordTxtToDatabase import initializeWordDatabase

@csrf_exempt
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def basikosAI(request):
    response = HttpResponse(content_type="application/json")

    if(request.method == "POST"):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        wordlist = list()
        w1 = databaseCommands.select_game_square(5066)
        w2 = databaseCommands.select_game_square(5065)
        wordlist.append(w1)
        wordlist.append(w2)

        print(databaseCommands.create_clue(210,"HumanG", "HumanP", "Yolo", wordlist, 2,"R",2,1))

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
        print(body)
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

        print(body)

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

        clue = JSONParser.deserializeClueAndCreateClue(body)

        response = HttpResponse(clue.clueID, status=201)

    else:
        return HttpResponse("Method not Allowed", status=405)

    return response

@csrf_exempt
def agentBasikosClue(request):

    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        game = JSONParser.deserializeGameSettingsAndCreateGame(body)
        agentI = BasikosAI(game)

        response = HttpResponse(agentI, content_type="application/json")

    else:
        return HttpResponse("Method not Allowed", status=405)

    return response

@csrf_exempt
def wordService(request):

    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        game = JSONParser.deserializeGameSettingsAndCreateGame(body)
        dump = json.dumps(game.serialiseGame())

        response = HttpResponse(dump, content_type="application/json")

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