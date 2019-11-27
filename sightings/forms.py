from django.forms import ModelForm
from sightings.models import Squirrel

class AddForm(ModelForm):
    class Meta:
        model = Squirrel
        fields = ['unique_squirrel_id', 'latitude', 'longitude', 
        'shift', 'date', 'age', 'primary_fur_color', 'location',
        'specific_location', 'running', 'chasing', 'climbing','eating',
        'foraging', 'other_activities', 'kuks', 'quaas','moans',
        'tail_flags', 'tail_twitches', 'approaches','indifferent',
         'runs_from']

    def __init__(self, *args, **kwargs):
        super(AddForm, self).__init__(*args, **kwargs)
        self.fields['latitude'].required = False
        self.fields['longitude'].required = False
        self.fields['shift'].required = False
        self.fields['date'].required = False
        self.fields['age'].required = False
        self.fields['primary_fur_color'].required = False
        self.fields['location'].required = False
        self.fields['specific_location'].required = False
        self.fields['running'].required = False
        self.fields['chasing'].required = False
        self.fields['climbing'].required = False
        self.fields['eating'].required = False
        self.fields['foraging'].required = False
        self.fields['other_activities'].required = False
        self.fields['kuks'].required = False
        self.fields['quaas'].required = False
        self.fields['moans'].required = False
        self.fields['tail_flags'].required = False
        self.fields['tail_twitches'].required = False
        self.fields['approaches'].required = False
        self.fields['indifferent'].required = False
        self.fields['runs_from'].required = False
        for field in self.fields:
            help_text = self.fields[field].help_text
            self.fields[field].help_text = None
