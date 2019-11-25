from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_sightings, name = 'all_sightings'),
    path('add/', views.add_sighting, name = 'add_sighting'),
    path('<str:unique_squirrel_id>/', views.sighting_details),
    # path('<str:unique_squirrel_id>/', views.DetailView.as_view(), name='detail'),
]

app_name = 'sightings'
