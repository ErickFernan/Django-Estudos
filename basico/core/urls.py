from django.urls import path

from .views import index, contato, produto  # O ponto é do módulo core

urlpatterns = [
    path('', index, name='index'),  # Se for na raiz mando pro index
    path('contato', contato, name='contato'),  # Se for no contato manda pro contato
    path('produto/<int:pk>', produto, name='xuxa'),
]