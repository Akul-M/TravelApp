from django.http import HttpResponse
from django.shortcuts import render
from . models import Destinations, Teams


# Create your views here.


def home(request):
    objects = Destinations.objects.all()
    teamObj = Teams.objects.all()
    return render(request, "index.html", {'data': objects, 'teamData': teamObj})
