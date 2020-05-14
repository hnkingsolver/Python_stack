from django.urls import path
from . import views
urlpatterns = [
    path('', views.login_reg),
    path ('register', views.register),
    path ('login', views.Login),
    path ('books', views.all_books),
    path ('books/add', views.addBook),
    path ('books/create', views.createBook),
    path ('books/<int:id>', views.newBook),

]