from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Book(models.Model):
    title =        models.CharField(max_length=200)
    author =       models.CharField(max_length=200)
    release_date = models.DateField()
    rank =        models.IntegerField()

    def __str__(self):
        return self.title

class User(models.Model):

    name =     models.CharField(max_length=200)
    surname =  models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email =    models.EmailField()
    age =      models.IntegerField()
    gender = models.CharField(max_length=50)
class Post:
    pass

class Author(models.Model):
    name =     models.CharField(max_length=200)
    surnname = models.CharField(max_length=200)
    date_of_birth = models.DateTimeField(blank=True,null=True)
    date_of_death = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name+" "+self.surname


class Comment():
    post=models.ForeignKey('blog.Post',related_name="comments",on_delete=True)
    author=models.CharField(max_length=200)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now())
    approved_comment=models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absoltle_url(self):
        return reverse("post_list")


    def __str__(self):
        return self.text
