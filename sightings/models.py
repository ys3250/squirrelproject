from django.db import models
from django.utils.translation import gettext as _
from django_pandas.managers import DataFrameManager
# from django.core.validators import RegexValidator

class Squirrel(models.Model):

    objects = DataFrameManager()

    def __str__(self):
        return self.unique_squirrel_id

    unique_squirrel_id = models.CharField(
        max_length = 100,
        help_text = _('Unique Squirrel ID'),
        unique = True,
        primary_key = True,
        # validators = [RegexValidator(
        # regex='^(\d{1,2}[A-Z])-(PM|AM)-(0[1-9]|1[0-2])([0-5][0-9])-(\d{2})',
        # message='unique squirrel id must be in form',
        # code='invalid_id'
        # ),],
    )

    morning = 'AM'
    afternoon = 'PM'

    shift_choices = (
        (morning, 'AM'),
        (afternoon, 'PM'),
    )

    shift = models.CharField(
        max_length = 2,
        choices = shift_choices,
        default = morning,
        help_text = _('AM/PM'),
        null = True,
    )

    date = models.DateTimeField(
        help_text = _('Date'),
        null = True,
    )

    age = models.CharField(
        max_length = 10,
        help_text = _('Age'),
        null = True,
    )

    latitude = models.FloatField(
        max_length = 20,
        help_text =_('Latitude'),
        null = True,
    )

    longitude = models.FloatField(
        max_length = 20,
        help_text =_('Longtitude'),
        null = True,
    )

    primary_fur_color = models.CharField(
        max_length = 100,
        help_text = _('Primary Fur Color'),
        null = True,
    )

    location = models.CharField(
        max_length = 100,
        help_text = _('Location'),
        null = True,
    )

    specific_location = models.CharField(
        max_length = 100,
        help_text = _('Specific Location'),
        null = True,
    )

    t = 'true'
    f = 'false'
    n = ''
    True_False = (
        (t, 'true'),
        (f, 'false'),
        (n, ''),
    )

    running = models.CharField(
        max_length = 10,
        choices = True_False,
        default = n,
        help_text = _('TRUE/FALSE'),
        null = True,
    )

    chasing = models.CharField(
        max_length = 10,
        choices = True_False,
        default = n,
        help_text = _('TRUE/FALSE'),
        null = True,
    )

    climbing = models.CharField(
        max_length = 10,
        choices = True_False,
        default = n,
        help_text = _('TRUE/FALSE'),
        null = True,
    )

    eating = models.CharField(
        max_length = 10,
        choices = True_False,
        default = n,
        help_text = _('TRUE/FALSE'),
        null = True,
    )

    foraging = models.CharField(
        max_length = 10,
        choices = True_False,
        default = n,
        help_text = _('TRUE/FALSE'),
        null = True,
    )

    other_activities = models.CharField(
        max_length = 100,
        help_text = _('Other Activities'),
        null = True,
    )

    kuks = models.CharField(
        max_length = 10,
        choices = True_False,
        default = n,
        help_text = _('TRUE/FALSE'),
        null = True,
    )

    quaas = models.CharField(
        max_length = 10,
        choices = True_False,
        default = n,
        help_text = _('TRUE/FALSE'),
        null = True,
    )

    moans = models.CharField(
        max_length = 10,
        choices = True_False,
        default = n,
        help_text = _('TRUE/FALSE'),
        null = True,
    )

    tail_flags = models.CharField(
        max_length = 10,
        choices = True_False,
        default = n,
        help_text = _('TRUE/FALSE'),
        null = True,
    )

    tail_twitches = models.CharField(
        max_length = 10,
        choices = True_False,
        default = n,
        help_text = _('TRUE/FALSE'),
        null = True,
    )

    approaches = models.CharField(
        max_length = 10,
        choices = True_False,
        default = n,
        help_text = _('TRUE/FALSE'),
        null = True,
    )

    indifferent = models.CharField(
        max_length = 10,
        choices = True_False,
        default = n,
        help_text = _('TRUE/FALSE'),
        null = True,
    )

    runs_from = models.CharField(
        max_length = 10,
        choices = True_False,
        default = n,
        help_text = _('TRUE/FALSE'),
        null = True,
    )
# Create your models here.
