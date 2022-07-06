from django.db import models

from accounts.models import User

class Course(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    tutor = models.ForeignKey(User, on_delete=models.CASCADE)
    weeks = models.IntegerField()
    price = models.IntegerField()
    
    def __str__(self):
        return self.name

    
    @property
    def get_duration(self):
        return f"{self.weeks} weeks"

class Track(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100, blank=True)
    courses = models.ManyToManyField(Course) # A track can contain many courses and many course can be in a track

    def __str__(self):
        return self.name
    

    # courses = Course

class CourseMaterial(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    
    @property
    def get_type(self):
        return 'generic'

class CourseVideo(CourseMaterial):
    video = models.FileField(upload_to='videos') # will later update it to use google storage
   
   
    def get_type(self):
        return 'video'


class CourseFile(CourseMaterial):
    file = models.FileField(upload_to='course_materials/files')

    def get_type(self):
        return 'file'


class CoursePost(CourseMaterial):
    message = models.TextField()
    file = models.ForeignKey(CourseFile, on_delete=models.SET_NULL, blank=True, null=True)

    def get_type(self):
        return 'post'

class CapstoneProject(models.Model):
    title = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    instruction = models.TextField()
    file_url = models.FileField(upload_to='capston-projects', null=True, blank=True)

    def __str__(self):
        return self.title
    

# This is to enable chatting between the admins and the tutors
class AdminChat(models.Model):
    message = models.TextField()
    is_read = models.BooleanField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reciever')

    def __str__(self):
        return f"Message from {self.sender.username}"
        

class Voucher(models.Model):
    code = models.CharField(max_length=7)
    percentage = models.IntegerField()
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return self.code
    