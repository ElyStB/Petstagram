from django.urls import path, include
from petstagram.photos.views import details_photo, edit_photo, CreatePetPhotoView

urlpatterns = (
    path("create/", CreatePetPhotoView.as_view(), name="create photo"),
    path(
        "<int:pk>/", include([
        path("", details_photo, name="details photo"),
        path("edit/", edit_photo, name="edit photo"),
        ]),
    ),
)
