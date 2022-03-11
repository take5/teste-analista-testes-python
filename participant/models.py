from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Participant(models.Model):
    name = models.CharField(_('Nome'), max_length=256, blank=False, null=False)
    age = models.IntegerField(_('Idade'), blank=False, null=False)