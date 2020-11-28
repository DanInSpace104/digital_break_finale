from django.db import models
from django.db.models.query import QuerySet
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.CASCADE
    )
    picture = models.ImageField(upload_to='profiles', default='profiles/default.png')

    def __str__(self):
        return self.user.username
