from django.urls import path
from . import views	

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('groups', views.groups),
    path('postgroup', views.post_group),
    path('groups/<int:id>', views.viewGroup),
    path('joingroup/<int:id>', views.joinGroup),
    path('unjoingroup/<int:id>', views.unJoinGroup),
    path('groups/delete/<int:id>', views.deleteGroup),
]