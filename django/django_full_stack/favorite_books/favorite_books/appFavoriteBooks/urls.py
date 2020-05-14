from django.urls import path
from . import views
urlpatterns = [
    path('', views.login_reg),
    path ('register', views.register),
    path ('login', views.Login),
    path ('all_books', views.all_books),
    path ('logout', views.logout),
    path ('add_book', views.add_book),
    path ('addFavorite/<int:id>', views.addFavorite),
    path ('view/<int:id>', views.viewBook),
    path ('book/<int:id>', views.userBook),
    path ('updateBook/<int:id>', views.updateBook),
    path ('deleteBook/<int:id>', views.deleteBook),
    path ('unFavorite/<int:id>', views.unFavorite),
    path ('listOfBooks/<int:id>', views.listOfBooks),
]