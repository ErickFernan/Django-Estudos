from django.urls import path

from .views import index, contato  # O ponto é do módulo core

urlpatterns = [
    path('', index),  # Se for na raiz mando pro index
    path('contato', contato),  # Se for no contato manda pro contato
]