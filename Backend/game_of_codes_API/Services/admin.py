from django.contrib import admin

from .models import Word
from .models import Agent
from .models import Clue
from .models import Game
from .models import Game_Square

admin.site.register(Word)
admin.site.register(Agent)
admin.site.register(Clue)
admin.site.register(Game)
admin.site.register(Game_Square)

