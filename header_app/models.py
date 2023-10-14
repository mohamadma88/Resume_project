from django.db import models


class Header(models.Model):
    name = models.CharField(max_length=30)
    text = models.TextField()

    def __str__(self):
        return self.name
