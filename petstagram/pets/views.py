from django.shortcuts import render, redirect

from petstagram.pets.models import Pet
from petstagram.pets.forms import PetBaseForm, PetCreateForm


def create_pet(request):
    pet_form = PetBaseForm(request.POST or None)

    #if request.metod == 'POST':
    if pet_form.is_valid():
        created_pet = pet_form.save()
        return redirect(to='pet details', username='Diyan Kalaydzhiev', pet_slug=created_pet.slug)

    context = {
        'pet_form': pet_form,
    }
    return render(request, "pets/create_pet.html", context=context)


def pet_details(request, username, pet_slug):
    context = {
        'pet': Pet.objects.get(slug=pet_slug),
    }
    return render(request, "pets/pet_details.html", context)


def pet_edit(request, username, pet_slug):
    pet = Pet.objects.filter(slug=pet_slug).get()
    pet_form = PetBaseForm(request.POST or None, instance=pet)

    if request.method == 'POST':
        if pet_form.is_valid():
            pet_form.save()
            return redirect(to='pet details', username=username, pet_slug=pet_slug)

    context = {
        'pet_form': pet_form,
        'username': username,
        'pet': pet,
    }
    return render(request, "pets/pet_edit.html", context)


def pet_delete(request, username, pet_slug):
    context = {}
    return render(request, "pets/pet_delete.html", context)
