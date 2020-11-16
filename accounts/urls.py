from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginPage, name="login"),  
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name='home'),

    path('interessado/<str:pk>/', views.interessadopg, name='interessado'),
    path('criar_interessado/', views.criarInteressado, name='criar_interessado'),
    path('editar_interessado/<str:pk>/', views.editarInteressado, name='editar_interessado'),
    path('deletar_interessado/<str:pk>/', views.deleteInteressado, name='deletar_interessado'),
    path('interessadolist/', views.interessadolist, name='interessadoslist'),

    path('criar_processo/', views.criarProcesso, name='criar_processo'),
    path('ver_processo/<str:pk>/', views.verProcesso, name='ver_processo'),
    path('deletar_processo/<str:pk>/', views.deleteProcesso, name='deletar_processo'),
    path('processolist/', views.processolist, name='processoslist'),

    path('criar_terra/', views.criarTerra, name='criar_terra'),
    path('ver_terra/<str:pk>/', views.verTerra, name='ver_terra'),
    path('deletar_terra/<str:pk>/', views.deleteTerra, name='deletar_terra'),
    path('terraslist/', views.terralist, name='terraslist'),

    path('criar_setor/', views.criarSetor, name='criar_setor'),
    path('ver_setor/<str:pk>/', views.verSetor, name='ver_setor'),
    path('deletar_setor/<str:pk>/', views.deleteSetor, name='deletar_setor'),
    path('setorlist/', views.setorlist, name='setorlist'),

]