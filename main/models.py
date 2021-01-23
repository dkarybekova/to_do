from django.db import models

class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_favourite = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)
    
class Book(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    price = models.IntegerField()
    genre = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    year = models.IntegerField()
    date = models.DateField(auto_now_add=True)