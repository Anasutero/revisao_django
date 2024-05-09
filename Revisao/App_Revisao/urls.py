from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.abre_index,name='abre_index'),
    path('', views.listagem, name='listagem'),
    path('editar_cadastro/<int:id>',views.editar_cadastro,name='editar_cadastro'),
    path('excluir_pessoa/<int:id>',views.excluir_pessoa,name='excluir_pessoa')
]