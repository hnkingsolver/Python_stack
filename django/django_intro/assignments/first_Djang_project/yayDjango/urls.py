from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new',views.new),
    path('create',views.create),
    path('show/<number>',views.show),
    path('edit/<number>', views.edit),
    path('destroy/<number>',views.destroy),
]
