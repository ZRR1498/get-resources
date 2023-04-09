from django.db import models


class Data(models.Model):
    date = models.DateTimeField()
    value = models.FloatField()

    def __str__(self):
        return f'{self.date}: {self.value}'

    class Meta:
        unique_together = ('date', 'value')
        verbose_name = 'Data'
        ordering = ['-date']
