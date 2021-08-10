from django.db import models

# Create your models here.
class Job(models.Model):
    mode_choice = [("FT", "Full Time"),("PT","Part Time")]
    occupation = models.CharField(verbose_name="Occupation",max_length = 100)
    posts = models.IntegerField(verbose_name="Positions Available", max_length=4)
    sector = models.CharField(verbose_name="Job Dormain",max_length=100)
    organization = models.CharField(verbose_name="Organization Name",max_length=60)
    Location = models.CharField(verbose_name="Area Found", max_length=20)
    mode = models.CharField(max_length="15", null=False, blank=False,choice=mode_choice )
    description = models.TextField(verbose_name="Job Description")


