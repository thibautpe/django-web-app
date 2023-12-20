# ~/projects/django-web-app/merchex/listings/views.py

from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing
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

def hellomvt(request):
    bands = Band.objects.all()
   # return render(request, 'listings/hello.html')
   # return render(request,'listings/hello.html',{'first_band': bands[0]})
    return render(request,'listings/hello.html',context={'bands': bands})
def about(request):
    # return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')
    return render(request,'listings/about.html')
def contact(request):
     #return HttpResponse('<h1>Contactez nous</h1> <p>En cours</p>')
    return render(request,'listings/contact.html')

def listings(request):
    listings = Listing.objects.all()
    return render(request,'listings/listings.html',context={'listings': listings})
"""
   return HttpResponse(
        <h1>Listings !</h1>
        <p>Voici la liste :<p>
        <ul>
            <li>{listings[0].title}</li>
            <li>{listings[1].title}</li>
            <li>{listings[2].title}</li>
            <li>{listings[3].title}</li>
       </ul>)
"""