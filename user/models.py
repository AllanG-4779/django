from django.db import models
from django.contrib.auth.models import  User
from home.models import Job

# creating the profile for the user using one to one relationship between the profile and the user's account

class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    profile_image = models.ImageField(verbose_name="Image", default="profile_pics/default.jpg", blank=True, null=True, upload_to="profile_pics")

    def __str__(self):
        return f'{self.user} created'

    def props(self):
        return f'{self.user.first_name.capitalize()} {self.user.last_name.capitalize()}'
