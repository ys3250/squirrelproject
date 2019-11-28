from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Squirrel
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from sightings.forms import AddForm
from django_pandas.io import read_frame
import pandas as pd
import numpy as np

def view_map(request):
    response_text = 'map'
    length = len(Squirrel.objects.all())
    if request.method == 'POST':
        # if request.POST['view_option'] == 'view_100':
        # # try:
        #     coordinates = Squirrel.objects.all()[:100]
        #     #data from squirrelmodel
        # else:
        # # except:
        #     coordinates = Squirrel.objects.all()
        try:
            n = int(request.POST['view_option'])
            coordinates = Squirrel.objects.all()[:n]
        except:
            return HttpResponse('error')
    else:
        coordinates = Squirrel.objects.all()
    context = {
        'length': length,
        'coordinates': coordinates,
    }
    return render(request, 'sightings/map.html', context)

def all_sightings(request):
    response_text = 'Here are the sightings in our database!'
    sightings = Squirrel.objects.all()
    length = len(sightings)
    context = {
        'sightings': sightings,
        'length': length,
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
            return HttpResponse('Thanks! We have updated it!')
        else:
            return HttpResponse('Invalid Input (Wrong Data etc.)')
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
        'squirrel': squirrel.unique_squirrel_id,
    }
    try:
        if request.method == 'POST':
            # if request.POST['confirmation'] == 'yes':
            #     context['message'] = f'{unique_squirrel_id} is deleted'
            #     squirrel.delete()
            #     return render(request, 'sightings/delete.html', context)
            # else:
            #     return render(request, 'sightings/detail.html', {
            #         'squirrel': squirrel.unique_squirrel_id,
            #         'error_message': "Please confirm to delete!",
            #     })
            context['message'] = f'{unique_squirrel_id} is deleted'
            squirrel.delete()
            return render(request, 'sightings/delete.html', context)

    except:
        return HttpResponse("Please confirm to delete!!")

def stats(request):
    qs = Squirrel.objects.all()
    qs = Squirrel.objects.exclude(primary_fur_color__isnull = True).exclude(primary_fur_color = '').exclude(age__isnull = True).exclude(age = '?').exclude(age = '')
    df = read_frame(qs)
    # return HttpResponse(df.to_html())


    # df = qs.to_dataframe()
    # template = 'sightings/stats.html'
    # context = {
    #     'sightings': qs,
    # }

    df_pv = dict()
    
    df = read_frame(qs)
    rows = ['primary_fur_color','age']#,'location']
    #cols = ['shift','eating']
    pt = qs.to_pivot_table(values='unique_squirrel_id', rows=rows, aggfunc = 'count')
    
    df_pv['1'] = pt.to_html()

    df = read_frame(qs)
    rows = ['primary_fur_color','age']#,'location']
    #cols = ['shift','eating']
    pt2 = qs.to_pivot_table(values='unique_squirrel_id', rows=rows, aggfunc = 'count')

    df_pv['2'] = pt2.to_html()

    context = {'df_pv': df_pv}
    # return HttpResponse(pt.to_html())
    return render(request, 'sightings/stats.html', context)

