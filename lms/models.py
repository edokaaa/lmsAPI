from django.db import models
from django.utils.text import slugify


LOCATIONS = (
    ('ONL', 'Online'),
    ('PHY', 'Physical')
)

class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class Track(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=250, unique=True, null=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    

class Course(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    tutor = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="course_tutor")
    duration = models.IntegerField()
    slug = models.SlugField(max_length=250, unique=True)
    price = models.IntegerField()
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    img_url = models.CharField(max_length=255, blank=True)
    hero_url = models.CharField(max_length=255, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    location = models.CharField(choices=LOCATIONS, max_length=3, default='ONL')
    
    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.name)
    #     super().save(*args, **kwargs)
    
# MAT_TYPES = (
#     ('video', 'Video'),
#     ('document', 'Document'),
# )
# class CourseMaterial(models.Model):
#     title = models.CharField(max_length=30)
#     description = models.CharField(max_length=100, blank=True)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     material_type = models.CharField(max_length=50, choices=MAT_TYPES)
#     video = models.FileField(upload_to='course_materials/videos', blank=True, null=True) # will later update it to use google storage
#     document = models.FileField(upload_to='course_materials/files', blank=True, null=True)

#     def __str__(self):
#         return self.title

# class CapstoneProject(models.Model):
#     title = models.CharField(max_length=50)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     file_url = models.FileField(upload_to='capstone-projects', null=True, blank=True)

#     def __str__(self):
#         return self.title
    
# class Instruction(models.Model):
#     instruction = models.TextField()
#     project = models.ForeignKey(CapstoneProject, on_delete=models.CASCADE)


# # This is to enable chatting between the admins and the tutors
# class AdminChat(models.Model):
#     message = models.TextField()
#     is_read = models.BooleanField()
#     sender = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name='sender')
#     receiver = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name='reciever')

#     def __str__(self):
#         return f"Message from {self.sender.username}"
        

# class Voucher(models.Model):
#     code = models.CharField(max_length=7)
#     percentage = models.IntegerField()
#     is_used = models.BooleanField(default=False)

#     def __str__(self):
#         return self.code
    
