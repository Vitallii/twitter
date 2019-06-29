from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_edit, name='post_edit')
]