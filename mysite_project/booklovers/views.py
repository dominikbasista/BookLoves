from django.utils import timezone
from django.shortcuts import render
from mysite_project.booklovers.models import Book, Author, Post
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from mysite_project.booklovers.forms import PostForm
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import SignUpForm

# Create your views here.

class SignUpView(View):
    form_class = SignUpForm
    template_name = "templates.sign_up.html"
    #wyswietla formulaz
    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {"form":form})
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            name = form.cleaned_data("name")
            surname = form.cleaned_data("surname")
            username = form.cleaned_data("username")
            age = form.cleaned_data("age")
            gender = form.cleaned_data("gender")
            password = form.cleaned_data("password")

            user.save()




class AboutView(TemplateView):
     template_name="about.html"

class BooksListView(ListView):

    model = Book

    def get_query_set(self):
        return Book.object.filter(realise_date__lte=timezone.now().order_by('-realise_date'))
    #na górze jest to rodzaj zapytania sql wykonywane przez django mówi: zlap oboekt klasy Book
    #
    # __lte = lest then or equal


class AuthorListView(ListView):

    model = Author

    def get_query_set(self):
        return Author.object.filter(date_of_birth__lte = timezone.now().order_by('-date_of_birth'))


class PostListView(ListView):

    model = Post

    def get_query_set(self):
        return Post.object.filter(published_date__lte = timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin,CreateView):

    login_url = "/login/"
    redirect_field_name = "blog/post_detail.html"
    form_class = PostForm
    model = Post

class UpdatePostView(LoginRequiredMixin,UpdateView):

    login_url = "/login/"
    redirect_field_name = "blog/post_detail.html"
    form_class = PostForm
    model = Post

class DeletePostView(DeleteView,LoginRequiredMixin):

    model = Post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin, CreateView):

    login_url = "/login/"
    redirect_field_name = "blog/post_detail.html"
    model = Post

    def get_query_set(self):

        return Post.object.filter(published_date__isnull = True).order_by('published_date') # całkiem mozliwe że trzeba to napisac tak:-published_date



@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post, pk = pk)
