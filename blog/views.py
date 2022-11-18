from django.shortcuts import render, get_object_or_404
from django.utils import timezone


from .models import Animal, Equipement


# Create your views here.

def farm(request):
    animal = Animal.objects.filter()
    equipement = Equipement.objects.filter()

    return render(request, 'blog/farm.html', {'animal': animal, 'equipement': equipement})

def animals(request):
    animal = Animal.objects.filter()
    return render(request, 'blog/animals.html', {'animal': animal})

def animaldetail(request, id_animal):
    animal = get_object_or_404(Animal, id_animal=id_animal)
    lieu = animal.lieu
    return render(request, 'blog/animal_detail.html', {'animal': animal})

def equipements(request):
    equipement = Equipement.objects.filter()
    return render(request, 'blog/equipements.html', {'equipement': equipement})

def equipementdetail(request, id_equip):
    equipement = get_object_or_404(Equipement, id_equip=id_equip)
    animal = Animal.objects.filter(lieu = equipement.id_equip)
    return render(request, 'blog/equipement_detail.html', {'animal': animal, "equipement": equipement})



