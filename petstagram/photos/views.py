from django.shortcuts import render, redirect

from petstagram.pets.forms import PetCreateForm, PetEditForm
from petstagram.pets.models import Pet
from petstagram.photos.models import PetPhoto


def create_photo(request):
    #pet_form = PetCreateForm(request.POST or None)

    #if request.method == "POST":
        #if pet_form.is_valid():
            #pet_form.save()
            #return redirect('details profile', pk=1)

    context = {
        #'pet_form': pet_form,
    }
    return render(request, "photos/create_photo.html", context)


def details_photo(request, pk):
    context = {
        'pet_photo': PetPhoto.objects.get(pk=pk),
    }
    return render(request, "photos/details_photo.html", context)


def edit_photo(request: object, pk: object) -> object:
    contex = {

    }
    return render(request, "photos/edit_photo.html", contex)
