from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from forms import MoveForm
from blog.models import Animal, Equipement

# Create your views here.

def farm(request):
    animal = Animal.objects.filter()
    equipement = Equipement.objects.filter()

    return render(request, 'blog/farm.html', {'animal': animal, 'equipement': equipement})

def aproposde(request):
    return render(request, 'blog/aproposde.html')

def animals(request):
    animal = Animal.objects.filter()
    return render(request, 'blog/animals.html', {'animal': animal})

def animaldetail(request, id_animal):
    animal = get_object_or_404(Animal, id_animal=id_animal)
    lieuinitial = animal.lieu
    msg = ""
    if request.method == "POST":
        form = MoveForm(request.POST, instance=animal)
        if form.is_valid():
            ancien_lieu = get_object_or_404(Equipement, id_equip=lieuinitial.id_equip)
            nouveau_lieu = get_object_or_404(Equipement, id_equip=animal.lieu.id_equip)

            if ancien_lieu.id_equip == "nid":
                if nouveau_lieu.id_equip == "litière":
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
                        msg = "Désolé, " + animal.id_animal + " ne dort pas!"
                        form.save(commit=False)
                else:
                    if ancien_lieu.id_equip == nouveau_lieu.id_equip:
                        msg = "Il est déjà dans " + nouveau_lieu.id_equip + " veuillez choisir une autre activité!"
                    else:
                        msg = "Désolé, " + animal.id_animal + " est " + animal.etat + ". Il ne peut pas aller directement à " + nouveau_lieu.id_equip + "!"
                    animal.lieu.id_equip = ancien_lieu.id_equip
                    form.save(commit=False)
            elif ancien_lieu.id_equip == "litière":
                if nouveau_lieu.id_equip == "mangeoire":
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
                            animalmangeoire = get_object_or_404(Animal, lieu="mangeoire")
                            animal.lieu.id_equip = ancien_lieu.id_equip
                            msg = "Impossible, la mangeoire est actuellement occupée par " + animalmangeoire.id_animal + "."
                    else:
                        form.save(commit=False)
                        msg = "Désolé, " + animal.id_animal + " n'a pas faim!"
                else:
                    if ancien_lieu.id_equip == nouveau_lieu.id_equip:
                        msg = "Il est déjà dans " + nouveau_lieu.id_equip + " veuillez choisir une autre activité!"
                    else:
                        msg = "Désolé, " + animal.id_animal + " est " + animal.etat + ". Il ne peut pas aller directement à " + nouveau_lieu.id_equip + "!"
                    animal.lieu.id_equip = ancien_lieu.id_equip
                    form.save(commit=False)
            elif ancien_lieu.id_equip == "mangeoire" :
                if nouveau_lieu.id_equip == "roue":
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
                            animalroue = get_object_or_404(Animal, lieu="roue")
                            animal.lieu.id_equip = ancien_lieu.id_equip
                            msg = "Impossible, la roue est actuellement occupée par " + animalroue.id_animal + "."
                    else:
                        form.save(commit=False)
                        msg = "Désolé, " + animal.id_animal + " n'est pas en état de faire du sport!"
                else:
                    if ancien_lieu.id_equip == nouveau_lieu.id_equip:
                        msg = "Il est déjà dans " + nouveau_lieu.id_equip + " veuillez choisir une autre activité!"
                    else:
                        msg = "Désolé, " + animal.id_animal + " est " + animal.etat + ". Il ne peut pas aller directement à " + nouveau_lieu.id_equip + "!"
                    animal.lieu.id_equip = ancien_lieu.id_equip
                    form.save(commit=False)
            elif ancien_lieu.id_equip == "roue":
                if nouveau_lieu.id_equip == "nid":
                    if animal.etat == "fatigué":
                        nid = get_object_or_404(Equipement, id_equip="nid")
                        if nid.disponibilite == "libre":
                            animal.etat = "endormi"
                            animal.lieu.id_equip = "nid"
                            animal.save()
                            ancien_lieu.disponibilite = "libre"
                            ancien_lieu.save()
                            nouveau_lieu.disponibilite = "occupé"
                            nouveau_lieu.save()
                            form.save()
                        else:
                            form.save(commit=False)
                            animalnid = get_object_or_404(Animal, lieu="nid")
                            animal.lieu.id_equip = ancien_lieu.id_equip
                            msg = "Impossible, le nid est actuellement occupé par " + animalnid.id_animal + "."
                    else:
                        form.save(commit=False)
                        msg = "Désolé, " + animal.id_animal + " n'est pas fatigué!"
                else:
                    if ancien_lieu.id_equip == nouveau_lieu.id_equip:
                        msg = "Il est déjà dans " + nouveau_lieu.id_equip + " veuillez choisir une autre activité!"
                    else:
                        msg = "Désolé, " + animal.id_animal + " est " + animal.etat + ". Il ne peut pas aller directement à " + nouveau_lieu.id_equip + "!"
                    animal.lieu.id_equip = ancien_lieu.id_equip
                    form.save(commit=False)
            return render(request, 'blog/animal_detail.html', {'animal': animal, 'form': form, "msg": msg})
            #return redirect('animal_detail', id_animal = id_animal, msg = msg)
    else:
        form=MoveForm()
        return render(request, 'blog/animal_detail.html', {'animal': animal, 'form': form, "msg": msg})
        

def equipements(request):
    equipement = Equipement.objects.filter()
    return render(request, 'blog/equipements.html', {'equipement': equipement})

def equipementdetail(request, id_equip):
    equipement = get_object_or_404(Equipement, id_equip=id_equip)
    animal = Animal.objects.filter(lieu = equipement.id_equip)
    return render(request, 'blog/equipement_detail.html', {'animal': animal, "equipement": equipement})



