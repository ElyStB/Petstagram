from django.db import models

from petstagram.photos.models import PetPhoto


class PhotoComment(models.Model):
    MAX_COMMENT_TEXT_LENGTH = 300

    text = models.TextField(max_length=MAX_COMMENT_TEXT_LENGTH)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_photo = models.ForeignKey(PetPhoto, on_delete=models.CASCADE)


class PhotoLike(models.Model):
    to_photo = models.ForeignKey(PetPhoto, on_delete=models.CASCADE)

