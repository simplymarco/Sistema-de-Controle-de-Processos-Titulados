from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('interessado/<str:pk>/', views.interessadopg, name='interessado'),
    path('criar_interessado/', views.criarInteressado, name='criar_interessado'),

    path('criar_processo/', views.criarProcesso, name='criar_processo'),
    path('ver_processo/<str:pk>/', views.verProcesso, name='ver_processo'),
    path('deletar_processo/<str:pk>/', views.deleteProcesso, name='deletar_processo'),

    path('criar_terra/', views.criarTerra, name='criar_terra'),
    path('ver_terra/<str:pk>/', views.verTerra, name='ver_terra'),
    path('deletar_terra/<str:pk>/', views.deleteTerra, name='deletar_processo'),
    path('terra/', views.terrapg, name='terra'),

]