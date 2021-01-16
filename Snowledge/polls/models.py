from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.http import HttpResponse

class Tag(models.Model):
    content = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return '{}'.format(self.content)

class Members(models.Model):
    role = models.CharField(max_length=50, null=False)
    django_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='django_user', null = False, blank=True)

class Question(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='owner', null = True, blank=True)
    title = models.CharField(max_length=200, null=False)
    content = models.CharField(max_length=3000, null=False)
    tags = models.ManyToManyField(Tag)
    date_created = models.DateTimeField(auto_now=True)
    solved = models.BooleanField(default = False, null = True)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ('-date_created',)

class Answer(models.Model):
    owner = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='my_question', null = True, blank=True)
    owner_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='owner_user', null = True, blank=True)
    content = models.CharField( max_length=3000, null=True)
    likes = models.IntegerField(default = 0, null=True, blank = True)
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('likes',)   #not sure if it work that way xd 

    def __str__(self):
        return '{}'.format(self.content)
    
