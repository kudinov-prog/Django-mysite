from django.urls import path

from .views import index, AdbCreateView

urlpatterns = [
    path('', index, name='index'),
    path('add/', AdbCreateView.as_view(), name='add'),
]