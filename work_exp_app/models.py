from django.db import models


class Work(models.Model):
    date = models.DateField(blank=True, null=True)
    exp = models.CharField(max_length=30, blank=True, null=True)
    grouping = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.exp
