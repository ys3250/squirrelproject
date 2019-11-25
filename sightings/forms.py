from django.forms import ModelForm
from sightings.models import Squirrel

class AddForm(ModelForm):
    class Meta:
        model = Squirrel
        fields = ['latitude', 'longitude', 'unique_squirrel_id',
        'shift', 'date', 'age', 'primary_fur_color', 'location',
        'specific_location', 'running', 'chasing', 'climbing','eating',
        'foraging', 'other_activities', 'kuks', 'quaas','moans',
        'tail_flags', 'tail_twitches', 'approaches','indifferent',
         'runs_from']
        help_texts = {'Latitude': '', 'Longitude': '',
         'Unique Squirrel ID': '', 'Shift': '', 'Date': 'DD/MM/YYYY',
         'Age': '', 'Primary Fur Color': '', 'Location': '',
         'Specific Location': '', 'Running': '', 'Chasing': '',
         'Climbing': '', 'Eating': '', 'Foraging': '',
         'Other Activities': '', 'Kuks': '', 'Quaas': '',
         'Moans': '', 'Tail flags': '', 'Tail twitches': '',
         'Approaches': '', 'Indifferent': '', 'Runs from': ''}
