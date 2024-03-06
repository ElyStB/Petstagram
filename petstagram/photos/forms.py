from django import forms

from petstagram.photos.models import PetPhoto


class PetPhotoCreateForm(forms.ModelForm):
    class Meta:
        model = PetPhoto
        fields = '__all__'
