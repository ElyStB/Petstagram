from django.urls import path

from petstagram.common.views import index, like_pet_photo, add_comment

urlpatterns = (
    path("", index, name="index"),
    path('pet_photo_like/<int:pk>', like_pet_photo, name='like_pet_photo'),
    path('comment/<int:pk>', add_comment, name='comment'),
)
