from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_sightings, name = 'all_sightings'),
    path('<str:unique_squirrel_id>/', views.sighting_details),
    path('add/',view.sighting_details),
]

app_name = 'sightings'
