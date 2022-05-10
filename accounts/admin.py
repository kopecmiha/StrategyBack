from django.contrib import admin

from accounts.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    User
    """

    list_display = "id", "username", "email"
    list_display_links = "id", "username", "email"
    search_fields = "id", "username"
