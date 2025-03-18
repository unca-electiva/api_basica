from django.http import JsonResponse, HttpResponseNotAllowed
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
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


@csrf_exempt
def modificar_consultar_eliminar_item(request, item_id):
    # Buscar el ítem por ID
    item = next((i for i in items if i["id"] == item_id), None)

    if not item:
        return JsonResponse({"error": "Ítem no encontrado"}, status=404)

    if request.method == 'GET':
        # Devolver los datos del ítem solicitado
        return JsonResponse(item)

    elif request.method == 'PUT':
        try:
            data = json.loads(request.body)
            item["nombre"] = data.get("nombre", item["nombre"])
            return JsonResponse(item)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Formato JSON inválido"}, status=400)

    elif request.method == 'DELETE':
        items.remove(item)
        return JsonResponse({"mensaje": "Ítem eliminado correctamente"}, status=204)

    else:
        return HttpResponseNotAllowed(['GET', 'PUT', 'DELETE'])

