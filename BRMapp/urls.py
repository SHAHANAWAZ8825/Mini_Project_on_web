from django.urls import re_path as url
from BRMapp import views

urlpatterns = [
     url('view-books',views.viewBooks),
     url('edit-book',views.editBook),
     url('delete-book',views.deleteBook),
     url('search-book',views.searchBook),
     url('new-book',views.newBook),
     url(r'^add',views.add),
     url('search',views.search),
     url('edit',views.edit),
     url('register',views.register),
     url('login',views.userLogin),
     url('logout',views.userLogout),
]
