from django.urls import path
from . import views

urlpatterns = [
    path('', views.farm, name='farm'),
    path('animal/<str:id_animal>/', views.animaldetail, name='animal_detail'),
    #path('animal/<str:id_animal>/?<str:message>', views.animal_detail, name='animal_detail_mes'),


]