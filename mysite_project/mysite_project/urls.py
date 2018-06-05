from django.contrib import admin
from django.conf.urls import url
#from mysite_project.booklovers.views import  BooksListView, AuthorListView


urlpatterns = [
    url(r'^admin/$', admin.site.urls),
    #url(r'^books_list$', BooksListView.as_view, name="books_list"),
    #url(r'^authors_list$',AuthorListView.as_view,name="author_list")

]
