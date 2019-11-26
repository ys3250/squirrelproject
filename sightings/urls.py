from django.urls import path

from . import views

urlpatterns = [
    path('sightings/', views.all_sightings, name = 'all_sightings'),
    path('map/', views.view_map, name = 'view_map'),
    path('sightings/add/', views.add_sighting, name = 'add_sighting'),
    path('sightings/<str:unique_squirrel_id>/', views.sighting_details),
    path('sightings/<str:unique_squirrel_id>/delete/', views.delete, name='delete'),
    # path('<str:unique_squirrel_id>/', views.DetailView.as_view(), name='detail'),
]

app_name = 'sightings'
