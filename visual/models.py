from random import randint

from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

def update_tag(val):
    tab = []
    for i in range(0, val):
        tab.append(randint(0, val))
    return tab


class Liste(models.Model):
    taille = models.IntegerField(default=100, null=True)
    tags = ArrayField(models.IntegerField(), null=True, blank=True)


    def __str__(self):
        return str(self.taille)

    def updateListe(self):
        tab = []
        for i in range(0, self.taille):
            tab.append(randint(0, self.taille))
        self.tags = tab
        return self.tags







