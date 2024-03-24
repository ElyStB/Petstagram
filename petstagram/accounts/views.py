from django.http import HttpResponseRedirect
from django.views import generic as views

from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views

from petstagram.accounts.forms import PetstagramUserCreationForm, PetstagramUserLoginForm, PetstagramProfileEditForm
from petstagram.accounts.models import Profile

UserModel = get_user_model()


class SignInUserView(auth_views.LoginView):
    form_class = PetstagramUserLoginForm
    template_name = "accounts/signin_user.html"

    def form_valid(self, form):
        super().form_valid(form)
        profile_instance, _ = Profile.objects.get_or_create(user=self.request.user)
        return HttpResponseRedirect(self.get_success_url())


class PetstagramUserRegisterView(views.CreateView):
    model = UserModel
    form_class = PetstagramUserCreationForm
    template_name = 'accounts/signup_user.html'
    success_url = reverse_lazy('index')


# def signin_user(request):
#    context = {}
#    return render(request, "accounts/signin_user.html", context)


class SignoutUserView(auth_views.LogoutView):
    pass


class ProfileDetailsView(views.DetailView):
    queryset = Profile.objects.prefetch_related('user').all()
    template_name = "accounts/details_profile.html"


class ProfileEditView(views.UpdateView):
    queryset = Profile.objects.all()
    form_class = PetstagramProfileEditForm
    template_name = "accounts/edit_profile.html"

    def get_success_url(self):
        return reverse_lazy(
            'details profile',
            kwargs={'pk': self.object.pk},
        )


class ProfileDeleteView(views.DetailView):
    queryset = Profile.objects.all()
    template_name = 'accounts/delete_profile.html'
