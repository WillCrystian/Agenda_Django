from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('busca/', views.busca, name='busca'),
    path('excluir/<int:contato_id>', views.excluir, name='excluir'),
    path('<int:contato_id>', views.detalhes, name='detalhes'),
]