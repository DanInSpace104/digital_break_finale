from django.db import models
from django.db.models.query import QuerySet
from django.conf import settings
from racs.models import Otdel


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.CASCADE
    )
    picture = models.ImageField(upload_to='profiles', default='profiles/default.png')
    otdel = models.ForeignKey(
        to='racs.Otdel', on_delete=models.PROTECT, related_name='profiles', blank=True, null=True
    )

    def __str__(self):
        return self.user.username
