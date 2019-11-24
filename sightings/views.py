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

def sighting_details(request, unique_squirrel_id):
    # sightings = Squirrel.objects.get(pk = unique_squirrel_id)
    squirrel = get_object_or_404(Squirrel, pk = unique_squirrel_id)
    return render(request, 'sightings/detail.html', {'squirrel': squirrel})
    # return HttpResponse(Squirrel.unique_squirrel_id)

class DetailView(generic.DetailView):
    model = Squirrel
    template_name = 'squirrel/detail.html'

def detail(request, unique_squirrel_id):
    squirrel = get_object_or_404(Squirrel, pk = unique_squirrel_id)
    return render(request, 'squirrel/detail.html', {'squirrel': squirrel})
# Create your views here.
