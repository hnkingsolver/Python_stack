from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('shows', views.Allshows),
    path('shows/add',views.Addshow),
    path('shows/create',views.createShow),
    path('shows/<int:id>', views.tvShow),
    path('shows/<int:id>/edit', views.editShow),
    path('shows/<int:id>/update', views.updateShow),
    path('shows/<int:id>/destroy', views.DeleteShow)
]