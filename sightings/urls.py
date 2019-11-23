from django.urls import path

from . import views

urlpatterns = [
    path('sightings/', views.all_sightings, name = 'all_sightings')
]

app_name = 'sightings'

