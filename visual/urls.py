from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('liste/', views.liste, name='liste'),
    path('newlist/', views.newlist, name='newlist'),
    path('newtag/<int:id>', views.newTag, name='newTag'),
    path('Insertionsort/<int:id>', views.Insertionsort, name='Insertionsort'),
    path('Bublesort/<int:id>', views.Bublesort, name='Bublesort'),
    path('Quicksort/<int:id>', views.Quicksort, name='Quicksort'),
    path('Selectiontionsort/<int:id>', views.Selectiontionsort, name='Selectiontionsort'),

]

#