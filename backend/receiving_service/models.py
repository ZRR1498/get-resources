from django.db import models


class Event(models.Model):
    date = models.DateTimeField(unique=True, verbose_name='Date event')

    def __str__(self):
        return f'{self.pk} {self.date}'

    class Meta:
        verbose_name = 'Event'
        ordering = ['-date']
