from django import forms
from django.forms import ModelForm
from .models import *


class createListe(ModelForm):

    class Meta:
        model = Liste
        fields = ['taille']



