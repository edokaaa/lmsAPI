from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from . models import User


# Register your models here.

class UsersAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_staff', 'is_student', 'is_tutor', 'last_login')
    search_fields = ('username', 'first_name')
    readonly_fields = ('is_staff', 'last_login', 'date_joined')
    filter_horizontal = ()
    list_filter = ('last_login',)
    fieldsets = ()
    ordering = ('username',)



admin.site.register(User, UsersAdmin)

