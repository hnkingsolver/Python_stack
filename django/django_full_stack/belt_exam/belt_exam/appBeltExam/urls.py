from django.urls import path
from . import views	

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path ('logout', views.logout),
    path('homepage', views.homepage),
    path('post_quote', views.post_quote),
    path('user/<int:id>', views.userPage),
    path('delete/<int:id>', views.deleteQuote),
    path('likeQuote/<int:id>', views.likeQuote),
    path ('unLikeQuote/<int:id>', views.unLikeQuote),
    path ('editaccount/<int:id>', views.editAccount),
    path ('updateAccount/<int:id>', views.updateAccount),
]