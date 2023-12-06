# ~/projects/django-web-app/merchex/listings/views.py

from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band

def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django !</h1>
        <p>Mes groupes préférés sont :<p>
        <ul>
            <li>{bands[0].name}</li>
            <li>{bands[1].name}</li>
            <li>{bands[2].name}</li>
        </ul>
""")

"""
Pour aider à la lisibilité, nous avons :
-utilisé des guillemets triples pour répartir notre chaîne HTML sur plusieurs lignes ;
-fait de cette chaîne une « f-string » afin que nous puissions injecter nos noms de groupes dans la chaîne en utilisant{ ... }comme placeholders.
"""

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def contact(request):
    return HttpResponse('<h1>Contactez nous</h1> <p>En cours</p>')

def listings(request):
    return HttpResponse('<h1>Listings</h1> <p>En cours</p>')