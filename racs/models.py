from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class Claim(models.Model):
    STATUS_CHOICES = (
        ('EX', 'Экспертиза'),
        ('DO', 'Доработка'),
        ('PR', 'Признано'),
        ('OT', 'Отклонено'),
        ('IP', 'Идёт опытное применение'),
        ('ON', 'Опытное применение завершено неуспешно'),
        ('OU', 'Опытное применение завершено успешно'),
        ('TU', 'Тиражирование завершено успешно'),
        ('TN', 'Тиражирование завершено неуспешно'),
    )
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='uclaims', verbose_name='Пользователи'
    )
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='EX')
    name = models.CharField(max_length=120)
    curr_desc = models.TextField()
    new_desc = models.TextField()
    pos_effect = models.TextField()
    costs = models.ManyToManyField('racs.Cost', related_name='claims', blank=True)
    terms = models.ManyToManyField('racs.Term', related_name='claims', blank=True)
    expert = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='eclaims', on_delete=models.PROTECT
    )
    category = models.ForeignKey('racs.Category', related_name='claims', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Cost(models.Model):
    name = models.CharField(max_length=255)
    summ = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class Term(models.Model):
    name = models.CharField(max_length=255)
    days = models.IntegerField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    expert = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='categories', on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name


class Otdel(models.Model):
    name = models.CharField(max_length=255)
    expert = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='otdels'
    )

    def __str__(self):
        return self.name
