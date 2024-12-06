from django.db import models


class Skill(models.Model):
    skill = models.CharField(max_length=200)

    def __str__(self):
        return self.skill


class Resume(models.Model):
    introducing = models.TextField()
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField()
    workexp = models.TextField()
    namecompany = models.CharField(max_length=200, null=True, blank=True)
    work = models.CharField(max_length=200, null=True, blank=True)
    textaward = models.TextField()
    skill = models.ManyToManyField(Skill,related_name='item')


    def __str__(self):
        return self.introducing
