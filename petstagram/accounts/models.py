from django.contrib.auth.hashers import make_password
from django.contrib.auth import models as auth_models, get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from petstagram.accounts.managers import PetstagramUserManager

"""
class PetstagramUserManager(auth_models.BaseUserManager):
    def create_user(self, email, password, **extra_fields):
    
        # Create and save a user with the given email, and password.
    
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)
"""


  # auth_models.AbstractUser
class PetstagramUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):

    email = models.EmailField(
        _("email address"),
        unique=True,
        null=False,
        blank=False,
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = PetstagramUserManager()


# PetstagramUser = get_user_model()


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30

    user = models.OneToOneField(
        PetstagramUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    first_name = models.CharField(max_length=FIRST_NAME_MAX_LENGTH, null=True, blank=True)
    last_name = models.CharField(max_length=LAST_NAME_MAX_LENGTH,null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.URLField(null=True, blank=True)

    @property
    def full_profile_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"

        return self.first_name or self.last_name
