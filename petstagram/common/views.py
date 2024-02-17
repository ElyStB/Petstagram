from django.shortcuts import render

from petstagram.photos.models import PetPhoto


def index(request):
    context = {
        'pet_photo': PetPhoto.objects.all(),

    }
    return render(request, "common/index.html", context=context)
