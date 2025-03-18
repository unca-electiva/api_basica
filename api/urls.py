from django.urls import path
from .views import obtener_agregar_items, modificar_consultar_eliminar_item

urlpatterns = [
    path('items/', obtener_agregar_items, name='obtener_agregar_items'),
    path('items/<int:item_id>/', modificar_consultar_eliminar_item, name='modificar_consultar_eliminar_item'),
]
