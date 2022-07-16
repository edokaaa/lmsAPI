from django.contrib import admin
from . models import CapstoneProject, CourseFile, CourseMaterial, CoursePost, CourseVideo, Track, Course, Voucher, Tag

# Django comes with a builtin admin dashboard,
# this file enable us to customise it


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'tutor')


class CourseMaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'course', 'get_type')


admin.site.register(Course, CourseAdmin)
admin.site.register(CourseMaterial, CourseMaterialAdmin)
admin.site.register(Track)
admin.site.register(CourseVideo)
admin.site.register(CourseFile)
admin.site.register(CoursePost)
admin.site.register(CapstoneProject)
admin.site.register(Voucher)

admin.site.register(Tag)