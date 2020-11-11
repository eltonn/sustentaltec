from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from sustentaltec.forms import UserChangeForm, UserCreationForm
from sustentaltec.models import Organization, User
from sustentaltec.admin_config import admin_site

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    class Meta:
        model = User


class OrganizationAdmin(admin.ModelAdmin):
    ...


admin_site.register(User, UserAdmin)
admin_site.register(Organization, OrganizationAdmin)
