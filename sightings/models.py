from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):

    def __str__(self):
        return self.unique_squirrel_id

    unique_squirrel_id = models.CharField(
        max_length = 100,
        help_text = _('Unique Squirrel ID'),
    )

    morning = 'AM'
    afternoon = 'PM'

    shift_choices = [
        (morning, 'AM'),
        (afternoon, 'PM'),
    ]

    shift = models.CharField(
        max_length = 2,
        choices = shift_choices,
        default = morning,
        help_text = _('AM/PM')
    )

    date = models.DateTimeField(
        help_text = _('Date'),
    )

    age = models.CharField(
        max_length = 10,
        help_text = _('Age'),
    )

    latitude = models.FloatField(
        max_length = 20,
        help_text =_('Latitude'),
    )

    Longtitude = models.FloatField(
        max_length = 20,
        help_text =_('Longtitude'),
    )

    primary_fur_color = models.CharField(
        max_length = 100,
        help_text = _('Primary Fur Color'),
    )

    location = models.CharField(
        max_length = 100,
        help_text = _('Location'),
    )

    specific_location = models.CharField(
        max_length = 100,
        help_text = _('Specific Location'),
    )

    true = 'TRUE'
    false = 'FALSE'
    none = ''
    True_False = [
        (true, 'TRUE'),
        (false, 'FALSE'),
        (none, ''),
    ]

    Running = models.CharField(
        max_length = 10,
        choices = True_False,
        default = none,
        help_text = _('TRUE/FALSE'),
    )

    Chasing = models.CharField(
        max_length = 10,
        choices = True_False,
        default = none,
        help_text = _('TRUE/FALSE'),
    )

    Climbing = models.CharField(
        max_length = 10,
        choices = True_False,
        default = none,
        help_text = _('TRUE/FALSE'),
    )

    Eating = models.CharField(
        max_length = 10,
        choices = True_False,
        default = none,
        help_text = _('TRUE/FALSE'),
    )

    Foraging = models.CharField(
        max_length = 10,
        choices = True_False,
        default = none,
        help_text = _('TRUE/FALSE'),
    )

    other_activities = models.CharField(
        max_length = 100,
        help_text = _('Other Activities'),
    )

    kuks = models.CharField(
        max_length = 10,
        choices = True_False,
        default = none,
        help_text = _('TRUE/FALSE'),
    )

    quaas = models.CharField(
        max_length = 10,
        choices = True_False,
        default = none,
        help_text = _('TRUE/FALSE'),
    )

    moans = models.CharField(
        max_length = 10,
        choices = True_False,
        default = none,
        help_text = _('TRUE/FALSE'),
    )

    tail_flags = models.CharField(
        max_length = 10,
        choices = True_False,
        default = none,
        help_text = _('TRUE/FALSE'),
    )

    tail_twitches = models.CharField(
        max_length = 10,
        choices = True_False,
        default = none,
        help_text = _('TRUE/FALSE'),
    )

    approaches = models.CharField(
        max_length = 10,
        choices = True_False,
        default = none,
        help_text = _('TRUE/FALSE'),
    )

    indifferent = models.CharField(
        max_length = 10,
        choices = True_False,
        default = none,
        help_text = _('TRUE/FALSE'),
    )

    runs_from = models.CharField(
        max_length = 10,
        choices = True_False,
        default = none,
        help_text = _('TRUE/FALSE'),
    )

# Create your models here.
