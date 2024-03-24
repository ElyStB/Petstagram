
from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms

from petstagram.accounts.models import Profile

UserModel = get_user_model()


class PetstagramUserCreationForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email', )


class PetstagramUserLoginForm(auth_forms.AuthenticationForm):
    username = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )


class PetstagramUserChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = UserModel
        fields = '__all__'


class PetstagramProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'date_of_birth', 'profile_picture']
        labels = {
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'date_of_birth': 'Date of Birth:',
            'profile_picture': 'Profile Picture:',
        }
