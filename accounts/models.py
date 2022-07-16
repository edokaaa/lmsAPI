from django.db import models
from django.contrib.auth.models import AbstractUser
import lms
from lms.models import Course, Track


class User(AbstractUser):
    # is_admin = models.BooleanField(default=False)
    # is_tutor = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=14, blank=True)
    photo = models.ImageField(upload_to='profile_images', blank=True)
    # username = None

    def __str__(self):
        return self.username
    
class Tutor(User):
    courses = models.ManyToManyField("lms.Course", blank=True, null=True, related_name="tutor_courses")

    def get_courses_count(self):
        no_of_course = Course.objects.all().filter(id=self.id).count
        return(no_of_course)


class Student(User):
    track = models.ForeignKey(Track, on_delete=models.CASCADE, blank=True, null=True)
    courses = models.ManyToManyField("lms.Course", blank=True, null=True)

    def get_discount(self):
        # till we figure out how to calculate the discount
        discount = 0
        return discount
    
    def get_enrolled_courses(self):
        user_courses = self.courses
        # logic pending
        return user_courses



    
