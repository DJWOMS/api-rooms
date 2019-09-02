from django.urls import path
from . import views

urlpatterns = [
    path('', views.RoomRecord.as_view()),
]