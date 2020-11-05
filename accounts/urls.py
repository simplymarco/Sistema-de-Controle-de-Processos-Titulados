from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('interessado/', views.interessado),
    path('terra/', views.terra),

]