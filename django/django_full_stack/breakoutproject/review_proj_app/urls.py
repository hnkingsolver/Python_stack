from django.urls import path
from . import views	

urlpatterns = [
    path('', views.index),
    path('users', views.createUser),
    path('login', views.login),
    path('homepage', views.homepage),
    path('cats', views.createCat),
    path('deleteCat/<int:id>', views.deleteCat),
    path('VoteCat/<int:id>', views.VoteCat),
    path ('unVoteCat/<int:id>', views.unVoteCat),
    path('profile', views.userProfile),
    path('cat/<int:id>', views.catProfile),
]