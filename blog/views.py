from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from forms import MoveForm
from blog.models import Animal, Equipement

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
    lieuinitial = animal.lieu

    if request.method == "POST":
        form = MoveForm(request.POST, instance=animal)
        if form.is_valid():
            ancien_lieu = get_object_or_404(Equipement, id_equip=lieuinitial.id_equip)
            nouveau_lieu = get_object_or_404(Equipement, id_equip=animal.lieu.id_equip)

            if ancien_lieu.id_equip == "nid" and nouveau_lieu.id_equip == "litière":
                if animal.etat == "endormi":
                    animal.etat = "affamé"
                    animal.lieu.id_equip = "litière"
                    ancien_lieu.disponibilite = "libre"
                    ancien_lieu.save()
                    animal.save()
                    nouveau_lieu.disponibilite = "occupé"
                    nouveau_lieu.save()
                    form.save()
                else:
                    #msg Désolé, il ne dort pas!
                    form.save(commit=False)
            if ancien_lieu.id_equip == "litière" and nouveau_lieu.id_equip == "mangeoire":
                if animal.etat == "affamé":
                    mangeoire = get_object_or_404(Equipement, id_equip="mangeoire")
                    if mangeoire.disponibilite == "libre":
                        animal.etat = "repus"
                        animal.lieu.id_equip = "mangeoire"
                        animal.save()
                        nouveau_lieu.disponibilite = "occupé"
                        nouveau_lieu.save()
                        if Animal.objects.filter(lieu = "litière").count == 0:
                            ancien_lieu.disponibilite = "libre"
                        else:
                            ancien_lieu.disponibilite = "occupé"
                        ancien_lieu.save()
                        form.save()
                    else:
                        form.save(commit=False)
                        #msg Impossible, la mangeoire est actuellement occupée par XXX
                else:
                    form.save(commit=False)
                    #msg Désolé, XXX n'a pas faim! 
            if ancien_lieu.id_equip == "mangeoire" and nouveau_lieu.id_equip == "roue":
                if animal.etat == "repus":
                    roue = get_object_or_404(Equipement, id_equip="roue")
                    if roue.disponibilite == "libre":
                        animal.etat = "fatigué"
                        animal.lieu.id_equip = "roue"
                        animal.save()
                        ancien_lieu.disponibilite = "libre"
                        ancien_lieu.save()
                        nouveau_lieu.disponibilite = "occupé"
                        nouveau_lieu.save()
                        form.save()
                    else:
                        form.save(commit=False)
                        #msg Impossible, la roue est actuellement occupée par XXX
                else:
                    form.save(commit=False)
                    #msg Désolé, XXX n'est pas en état de faire du sport!
            if ancien_lieu.id_equip == "roue" and nouveau_lieu.id_equip == "nid":
                if animal.etat == "fatigué":
                    nid = get_object_or_404(Equipement, id_equip="nid")
                    if nid.disponibilite == "libre":
                        animal.etat = "endormi"
                        animal.lieu.id_equip = "nid"
                        animal.save()
                        ancien_lieu = "libre"
                        ancien_lieu.save()
                        nouveau_lieu.id_equip = "occupé"
                        nouveau_lieu.save()
                        form.save()
                    else:
                        form.save(commit=False)
                        #msg Impossible, le nid est actuellement occupé par XXX
                else:
                    form.save(commit=False)
                    #msg Désolé, XXX n'est pas fatigué!
            return redirect('animal_detail', id_animal=id_animal)
    else:
        form=MoveForm()
        return render(request, 'blog/animal_detail.html', {'animal': animal, 'form': form})
        

def equipements(request):
    equipement = Equipement.objects.filter()
    return render(request, 'blog/equipements.html', {'equipement': equipement})

def equipementdetail(request, id_equip):
    equipement = get_object_or_404(Equipement, id_equip=id_equip)
    animal = Animal.objects.filter(lieu = equipement.id_equip)
    return render(request, 'blog/equipement_detail.html', {'animal': animal, "equipement": equipement})



