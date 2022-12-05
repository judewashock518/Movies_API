from django.urls import path
from . import views

urlpatterns = [
    path('', views.movies_list),
    path('<int:pk>/', views.movie_detail),
]