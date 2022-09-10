from django.contrib import admin
from . models import Track, Course,Tag

# Django comes with a builtin admin dashboard,
# this file enable us to customise it


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'tutor',)


admin.site.register(Course, CourseAdmin)
admin.site.register(Track)
admin.site.register(Tag)