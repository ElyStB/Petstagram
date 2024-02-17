from petstagram.pets.views import create_pet, pet_delete, pet_edit, pet_details
from django.urls import path, include

urlpatterns = (
    path("create/", create_pet, name="create pet"),
    path("<str:username>/pet/<slug:pet_slug>/",
        include([
            path("", pet_details, name="pet details"),
            path("edit/", pet_edit, name="pet edit"),
            path("delete/", pet_delete, name="pet delete"),
        ]),
    ),
    )
