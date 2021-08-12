from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class Job(models.Model):
    mode_choice = [("FT", "Full Time"), ("PT", "Part Time")]
    occupation = models.CharField(verbose_name="Occupation", max_length=100)
    posts = models.IntegerField(verbose_name="Positions Available", max_length=4)
    sector = models.CharField(verbose_name="Job Domain", max_length=100)
    organization = models.CharField(verbose_name="Organization Name", max_length=60)
    Location = models.CharField(verbose_name="Area Found", max_length=20)
    mode = models.CharField(max_length=15, null=False, blank=False, choices=mode_choice)
    description = models.TextField(verbose_name="Job Description")
    posted_on = models.DateField(verbose_name="Date", auto_now_add=True)
    deadline = models.DateField(verbose_name="Deadline")

    #  Adding a computed property
    def days_between(self):
        days =str(self.deadline - self.posted_on).split(" ")[0]
        return int(days)

    days_left = property(days_between)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.occupation} {self.days_left} day(s) left'
