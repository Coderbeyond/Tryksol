from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    otp = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=255,default=None)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):
        return self.name
    
class Quiz(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=255,default=None)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):
        return self.title
    
class Option(models.Model):
    question = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    option_text = models.CharField(max_length=255,default=None)
    is_correct_option = models.CharField(max_length=255,default=None)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True)


class Result(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    score = models.IntegerField(null=True)
    date_completed = models.DateTimeField(auto_now=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True)
