from django.db import models


class Award (models.Model):
    date = models.DateField()
    text = models.TextField()

    def __str__(self):
        return self.text