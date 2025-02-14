from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


# Base de datos en memoria (simulación)
items = [{"id": 1, "nombre": "Laptop"}, {"id": 2, "nombre": "Telefono"}]


@csrf_exempt # Desactiva la verificación CSRF para pruebas
def obtener_agregar_items(request):
    if request.method == 'GET':
        # Devolver la lista de ítems en formato JSON
        return JsonResponse(items, safe=False)
    elif request.method == 'POST':
        try:
            # Convertir el contenido JSON del cuerpo en diccionario
            data = json.loads(request.body)
            nuevo_item = {
                "id": len(items) + 1,
                "nombre": data.get("nombre", "Sin nombre")
            }
            # Agregar el nuevo ítem a la lista
            items.append(nuevo_item)
            # Respuesta satisfactoria con el objeto creado
            return JsonResponse(nuevo_item, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Formato JSON inválido"}, status=400)
