from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_sightings, name = 'all_sightings'),
    path('<str:unique_squirrel_id>/', views.sighting_details),
    # path('<str:unique_squirrel_id>/', views.DetailView.as_view(), name='detail'),
    path('add/',views.sighting_details),
]

app_name = 'sightings'
