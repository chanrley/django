from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_exemplos, name='lista_exemplos'),
    path('novo/', views.novo_exemplo, name='novo_exemplo'),
    path('edita/<int:id>/', views.edita_exemplo, name='edita_exemplo'),
    path('remove/<int:id>/', views.remove_exemplo, name='remove_exemplo'),
]

