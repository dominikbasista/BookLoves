from django.conf.urls import url
from mysite_project.booklovers.views import (AboutView, BooksListView, AuthorListView, PostDetailView, CreatePostView,
                                             UpdatePostView, DeletePostView, DraftListView,SignUpView)

urlpattern = [

    #url(r'^start$',)
    url(r'^about$', AboutView.as_view(), name="about"),
    url(r'^books_list/$', BooksListView.as_view, name="books_list"),
    url(r'^authors_list/$', AuthorListView.as_view, name="author_list"),
    url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view, name="post_detail"),
    url(r'^post/new/$', CreatePostView.as_view, name="new_post"),
    url(r'^post/(?P<pk>\d+)/edit/$', UpdatePostView, name="update_post"),
    url(r'^post/(?P<pk>\d+)/remove/$', DeletePostView, name="remove_post"),
    url(r'^drafts/$', DraftListView, name="post_draw_list"),
    url(r'^sign_up$', SignUpView, name="sign_up")
]