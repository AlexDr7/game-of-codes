import json

from django.http import HttpResponse
from django.views.decorators.cache import cache_control
from django.views.decorators.csrf import csrf_exempt

from Services.Models.Game import Game

@csrf_exempt
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def basikosAI(request):
    response = HttpResponse(content_type="application/json")

    if(request.method == "POST"):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        #raytracer = JSONParser().deserializeRayTracingTask(body)

        #img = raytracer.startRayTracing()

        #plt.imsave(response, img)
    else:
        return HttpResponse("Method not Allowed", status=405)

    return response


@csrf_exempt
def wordService(request):

    if request.method == "POST":
        #body_unicode = request.body.decode('utf-8')
        #body = json.loads(body_unicode)

        game = Game(8, 8)
        dump = json.dumps(game.serialiseGame())

        response = HttpResponse(dump, content_type="application/json")

        #raytracer = JSONParser().deserializeRayTracingTask(body)

        #img = raytracer.startRayTracing()

        #plt.imsave(response, img)
    else:
        return HttpResponse("Method not Allowed", status=405)

    return response
