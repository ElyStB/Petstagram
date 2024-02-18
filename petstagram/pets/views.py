from django.shortcuts import render

from petstagram.pets.models import Pet


def create_pet(request):
    context = {}
    return render(request, "pets/create_pet.html", context)


def pet_details(request, username, pet_slug):
    context = {
        'pet': Pet.objects.get(slug=pet_slug),
    }
    return render(request, "pets/pet_details.html", context)


def pet_edit(request, username, pet_slug):
    context = {}
    return render(request, "pets/pet_edit.html", context)


def pet_delete(request, username, pet_slug):
    context = {}
    return render(request, "pets/pet_delete.html", context)
