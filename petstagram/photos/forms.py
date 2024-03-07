from django import forms

from petstagram.photos.models import PetPhoto


class PetPhotoCreateForm(forms.ModelForm):
    class Meta:
        model = PetPhoto
        fields = '__all__'


class PetPhotoEditForm(forms.ModelForm):
    class Meta:
        model = PetPhoto
        exclude = ['photo']



