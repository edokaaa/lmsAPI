from django.db import models
from django.contrib.auth.models import AbstractUser, User


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_tutor = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Course(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    tutor = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class CourseVideo(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos') # will later update it to use google storage

    def __str__(self):
        return self.title

