from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('post/<int:pk>/', detail, name='detail'),
    path('post/new', new, name='new'),
    path('post/<int:pk>/edit/', edit, name='edit'),
    path('post/<int:pk>/delete/', delete, name='delete')
]
