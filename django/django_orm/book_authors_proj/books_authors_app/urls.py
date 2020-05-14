from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('add_book',views.add_book),
    path('show_book/<int:id>', views.show_book),
    path('add_a_b/<int:id>', views.add_a_b),
    path('author', views.author),
    path('add_author', views.add_author),
    path('show_author/<int:id>', views.show_author),
    path('add_b_a/<int:id>', views.add_b_a),
]