from django.urls import path
from .views import face_swap_api

urlpatterns = [
    path('face_swap/', face_swap_api, name='face_swap'),
]