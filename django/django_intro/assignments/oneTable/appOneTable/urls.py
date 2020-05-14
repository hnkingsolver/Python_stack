from django.urls import path
from . import views
urlpatterns = [
    path('', views.root),
    path('add',views.add),
    path('list', views.list),
    path('addPrisoner', views.addPrisoner),
    path('delete/<int:id>', views.delete),
]