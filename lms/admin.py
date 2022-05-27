from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import CapstoneProject, CourseFile, CourseMaterial, CoursePost, CourseVideo, Student,Track, User, Course

# Django comes with a builtin admin dashboard,
# this file enable us to customise it


class UsersAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_admin', 'is_tutor', 'is_staff', 'last_login')
    search_fields = ('username', 'first_name')
    readonly_fields = ('is_staff', 'last_login', 'date_joined')
    filter_horizontal = ()
    list_filter = ('last_login',)
    fieldsets = ()

    ordering = ('username',)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'tutor')


class CourseMaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'course', 'get_type')


admin.site.register(User, UsersAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseMaterial, CourseMaterialAdmin)
admin.site.register(Student)
admin.site.register(Track)
admin.site.register(CourseVideo)
admin.site.register(CourseFile)
admin.site.register(CoursePost)
admin.site.register(CapstoneProject)
