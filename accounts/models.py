from django.db import models
from django.contrib.auth.models import AbstractUser

from lms.models import Course, Track


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_tutor = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=14, blank=True)
    photo = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.username
    
    def user_type(self):
        if self.is_tutor:
            return 'Tutor'
        elif self.is_admin or self.is_staff:
            return 'Admin'
        else:
            return 'Student'


class Student(User):
    track = models.ForeignKey(Track, on_delete=models.CASCADE, blank=True, null=True)
    courses = models.ManyToManyField(Course, blank=True, null=True)

    def get_discount(self):
        # till we figure out how to calculate the discount
        discount = 0
        return discount
    
    def get_enrolled_courses(self):
        user_courses = Student.courses
        # logic pending
        return user_courses



    
