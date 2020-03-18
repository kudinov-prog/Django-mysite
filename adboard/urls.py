from django.urls import path

from .views import adboard_list, index

urlpatterns = [
    path('adboard/', adboard_list),
    path('main', index),
]