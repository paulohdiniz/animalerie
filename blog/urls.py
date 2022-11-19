from django.urls import path
from . import views

urlpatterns = [
    path('', views.farm, name='farm'),
    path('animals', views.animals, name = 'animals'),
    path('animal/<str:id_animal>/', views.animaldetail, name='animal_detail'),
    path('equipements', views.equipements, name = 'equipements'),
    path('equipements/<str:id_equip>/', views.equipementdetail, name='equipement_detail'),
    path('aproposde', views.aproposde, name='aproposde'),
    #path('animal/<str:id_animal>/?<str:message>', views.animal_detail, name='animal_detail_mes'),


]