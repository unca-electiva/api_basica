from django.urls import path
from .views import obtener_agregar_items

urlpatterns = [
    path('items/', obtener_agregar_items, name='obtener_agregar_items'),
]
