from django.shortcuts import render, redirect

from petstagram.pets.forms import PetCreateForm, PetEditForm
from petstagram.pets.models import Pet
from petstagram.photos.forms import PetPhotoCreateForm
from petstagram.photos.models import PetPhoto


def create_photo(request):
    photo_form = PetPhotoCreateForm(request.POST or None, request.FILES or None)

    if photo_form.is_valid():
        photo_form.save()
        return redirect('index')

    context = {
        'photo_form': photo_form,
    }
    return render(request, "photos/create_photo.html", context=context)


def details_photo(request, pk):
    context = {
        'pet_photo': PetPhoto.objects.get(pk=pk),
    }
    return render(request, "photos/details_photo.html", context)


def edit_photo(request: object, pk: object) -> object:
    contex = {

    }
    return render(request, "photos/edit_photo.html", contex)
