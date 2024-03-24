from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from petstagram.accounts.forms import PetstagramUserChangeForm, PetstagramUserCreationForm

PetstagramUser = get_user_model()


@admin.register(PetstagramUser)
class PetstagramUserAdmin(UserAdmin):
    model = PetstagramUser
    add_form = PetstagramUserCreationForm
    form = PetstagramUserChangeForm

    list_display = ('pk', 'email', 'is_staff', 'is_superuser')
    search_fields = ('email',)
    ordering = ('pk',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
        ('important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None,
         {
             'classes': ("wide",),
             'fields': ('email', 'password1', 'password2'),
         },
         ),
    )
