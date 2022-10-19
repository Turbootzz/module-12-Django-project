from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.overview, name='overview'),
    path('<int:games_id>', views.detail, name='detail'),
]
