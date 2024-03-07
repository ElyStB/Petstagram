from django.shortcuts import render, redirect

from petstagram.common.forms import CommentForm
from petstagram.pets.models import Pet
from petstagram.pets.forms import PetBaseForm, PetCreateForm, PetDeleteForm


def create_pet(request):
    pet_form = PetBaseForm(request.POST or None)

    # if request.method == 'POST':
    if pet_form.is_valid():
        created_pet = pet_form.save()
        return redirect(to='pet details', username='Diyan Kalaydzhiev', pet_slug=created_pet.slug)

    context = {
        'pet_form': pet_form,
    }
    return render(request, "pets/create_pet.html", context=context)


def pet_details(request, username, pet_slug):
    comment_form = CommentForm()

    context = {
        'pet': Pet.objects.get(slug=pet_slug),
        'comment_form': comment_form,
    }
    return render(request, "pets/pet_details.html", context)


def pet_edit(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'GET':
        pet_form = PetBaseForm(instance=pet, initial=pet.__dict__)

    else:
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
    return render(request, "pets/pet_edit.html", context=context)


def pet_delete(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'POST':
        pet.delete()
        return redirect('details profile', pk=1)

    pet_form = PetDeleteForm(initial=pet.__dict__)

    context = {
        'pet_form': pet_form,
        'username': username,
        'pet': pet,
    }
    return render(request, "pets/pet_delete.html", context=context)
