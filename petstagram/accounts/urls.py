from django.urls import path, include


from petstagram.accounts.views import \
    PetstagramUserRegisterView, SignInUserView, SignoutUserView, \
    ProfileDetailsView, ProfileEditView, ProfileDeleteView

urlpatterns = (
    path("signup/", PetstagramUserRegisterView.as_view(), name="signup user"),
    path("signin/", SignInUserView.as_view(), name="signin user"),
    path("signout/", SignoutUserView.as_view(), name="signout user"),
    path(
        "profile/<int:pk>/", include(
            [path("", ProfileDetailsView.as_view(), name="details profile"),
             path("edit/", ProfileEditView.as_view(), name="edit profile"),
             path("delete/", ProfileDeleteView.as_view(), name="delete profile"),]),
        )
    )
