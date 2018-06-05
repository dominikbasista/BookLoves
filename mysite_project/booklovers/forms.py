from django import forms
from mysite_project.booklovers.models import Post, Comment, User
from django.shortcuts import render,redirect

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["name","surname","username","age","gender","password"]






class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ("author","title","text")

    widget={
        "title":forms.TextInput(attrs={'class':'textinputclass'}),# ta klasa jest moja
        "text":forms.Textarea(attrs={"class": "editable medium-editor-textarea postcontent"}) #postcontent to tez moja klasa
    }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ("author","text")

    widget = {
        "title": forms.TextInput(attrs={'class': 'textinputclass'}),
        "text": forms.Textarea(attrs={"class": "editable medium-editor-textarea postcontent"})

    }