"""game_of_codes_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Services.Webservice import endpoint

urlpatterns = [
    path('basikosAI', endpoint.basikosAI, name='basikos'),
    path('wordService', endpoint.wordService, name='wordService'),
    path('addClue', endpoint.addClue, name='addClue'),
    path('updateClue', endpoint.updateClue, name='updateClue'),
    path('initializeDatabase', endpoint.initializeDatabase, name='initializeDatabase'),
    path('updateGame', endpoint.updateGame, name='updateGame'),
    path('guideBasikosAskClue', endpoint.guideBasikosAskClue, name='guideBasikosAskClue'),
    path('admin/', admin.site.urls),
]
