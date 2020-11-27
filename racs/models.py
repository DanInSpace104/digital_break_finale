from django.db import models


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
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
