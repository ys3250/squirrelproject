from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Squirrel
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from sightings.forms import AddForm

def all_sightings(request):
    response_text = 'Here are the sightings in our database!'
    sightings = Squirrel.objects.all()
    context = {
        'sightings': sightings,
    }
    return render(request, 'sightings/all.html', context)

def sighting_details(request, unique_squirrel_id):
    sightings = get_object_or_404(Squirrel, pk = unique_squirrel_id)
    form = AddForm(request.POST or None, instance=sightings)
    context = {
        'sightings': sightings,
        'form': form,
    }
    if request.method == 'POST' :
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return HttpResponse('thanks')
        else:
            return HttpResponse('invalid input')
    else:
        return render(request, 'sightings/detail.html', context)
    # return HttpResponse(Squirrel.unique_squirrel_id)

def add_sighting(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return render(request, 'sightings/returnhome.html')
        else:
            return HttpResponse('invalid input')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddForm()
        return render(request, 'sightings/addpage.html', {'form': form})

def delete(request, unique_squirrel_id):
    squirrel = get_object_or_404(Squirrel, pk = unique_squirrel_id)
    sightings = Squirrel.objects.all()
    context = {
        'sightings': sightings,
        'squirrel': squirrel.unique_squirrel_id
    }
    squirrel.delete()
    return render(request, 'sightings/delete.html', context)

# class DetailView(generic.DetailView):
#     model = Squirrel
#     template_name = 'squirrel/detail.html'

# def detail(request, unique_squirrel_id):
#     squirrel = get_object_or_404(Squirrel, pk = unique_squirrel_id)
#     return render(request, 'squirrel/detail.html', {'squirrel': squirrel})
# Create your views here.
