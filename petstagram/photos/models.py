from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_photo_size_less_than_5mb


class PetPhoto(models.Model):
    MAX_DESCRIPTION_SIZE = 300
    MAX_LOCATION_LENGTH = 30

    photo = models.ImageField(
        validators=(validate_photo_size_less_than_5mb,),
    )

    description = models.TextField(
        max_length=MAX_DESCRIPTION_SIZE,
        validators=(MinLengthValidator(10),),
        blank=True, null=True,
    )

    location = models.TextField(
        max_length=MAX_LOCATION_LENGTH,
        blank=True, null=True,
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )

    date_of_publication = models.DateField(
        auto_now=True,
    )
