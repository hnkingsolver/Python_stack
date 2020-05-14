from django.urls import path
from . import views

urlpatterns = [
    path('', views.firstFunction),
    path('second', views.secondFunction),
    path('hello/<str:name>', views.hello),
    path('template', views.template)
]