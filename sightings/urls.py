from django.urls import path

from . import views

urlpatterns = [
    path('sightings/', views.all_sightings, name = 'all_sightings'),
    path('<str:unique_squirrel_id>', views.sighting_details),
]

app_name = 'sightings'
