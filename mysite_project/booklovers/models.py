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


class Author(models.Model):
    name =     models.CharField(max_length=200)
    surnname = models.CharField(max_length=200)
    date_of_birth = models.DateTimeField(blank=True,null=True)
    date_of_death = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name+" "+self.surname

class Post():
    author = models.ForeignKey("auth.User")
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date=models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()


    def approve_coments(self):
        return self.comments.filter(approved_coments=True)

    def get_absolutle_url(self):
        return reverse("post_detail",{"pk":self.pk})

    def __str__(self):
        return self.title

class Comment():
    post=models.ForeignKey('blog.Post',related_name="comments")
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
