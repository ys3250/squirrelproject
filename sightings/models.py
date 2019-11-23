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
        help_text = _('Sighting Session Day and Month (23082019'),
    )
    age = models.IntegerField(
        help_text = _('Sighting Session Day and Month (23082019'),
    )
# Create your models here.
