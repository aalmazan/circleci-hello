from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Account


class AccountAdmin(UserAdmin):
    """Account admin."""
    pass


admin.register(Account, AccountAdmin)
