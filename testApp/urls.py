from django.urls import path
from .views import index, create

urlpatterns = [
    path('', index),
    path('create/', create),
]