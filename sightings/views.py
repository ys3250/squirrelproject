from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Squirrel
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

def all_sightings(request):
    response_text = 'Here are the sightings in our database!'
    sightings = Squirrel.objects.all()
    context = {
        'sightings': sightings,
    }
    return render(request, 'sightings/all.html', context)

def sighting_details(request, sightings_id):
    sightings = Squirrel.objects.get(id=sightings_id)
    return HttpResponse(Squirrel.unique_squirrel_id)
# Create your views here.
