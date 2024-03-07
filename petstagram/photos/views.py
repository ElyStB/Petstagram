from django.shortcuts import render, redirect

from petstagram.common.forms import CommentForm
from petstagram.photos.forms import PetPhotoCreateForm, PetPhotoEditForm
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
    comment_form = CommentForm()

    context = {
        'pet_photo': PetPhoto.objects.get(pk=pk),
        'comment_form': comment_form,
    }
    return render(request, "photos/details_photo.html", context)


def edit_photo(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    if request.method == "GET":
        photo_form = PetPhotoEditForm(instance=pet_photo, initial=pet_photo.__dict__)

    else:
        photo_form = PetPhotoEditForm(request.POST, instance=pet_photo)
        if request.method == "POST":
            if photo_form.is_valid():
                photo_form.save()
                return redirect('details photo', pk=pk)

    contex = {
        'photo_form': photo_form
    }
    return render(request, "photos/edit_photo.html", contex)
