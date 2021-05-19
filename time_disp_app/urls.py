from django.urls import path     
from . import views
urlpatterns = [
    path('time_disp', views.index),
]