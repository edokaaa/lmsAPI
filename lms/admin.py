from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import User, Course, CourseVideo

# Django comes with a builtin admin dashboard,
# this file enable us to customise it


class UsersAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_admin', 'is_tutor', 'is_student', 'is_staff', 'last_login')
    search_fields = ('username', 'first_name')
    readonly_fields = ('is_staff', 'last_login', 'date_joined')
    filter_horizontal = ()
    list_filter = ('last_login',)
    fieldsets = ()

    ordering = ('username',)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'tutor')


class CourseVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'course')


admin.site.register(User, UsersAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseVideo, CourseVideoAdmin)
