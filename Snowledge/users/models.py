from django.db import models
from django.contrib.auth.models import User
from polls.models import Tag


# Create your models here.
class UserSkills(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Tag)
