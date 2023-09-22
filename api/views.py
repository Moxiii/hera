from django.shortcuts import render
from rest_framework import viewsets
from api.models import Sneaker
from api.serializers import SneakerSerializer
from django.shortcuts import get_object_or_404
from django.views import View
from django.http import JsonResponse
# Create your views here.
class SneakerViewSet(viewsets.ModelViewSet):
    queryset = Sneaker.objects.all()
    serializer_class=SneakerSerializer

class GestionObjetView(View):
    def get(self, request, id, *args, **kwargs):
        objet = get_object_or_404(Sneaker, id=id)
        serialized_data = {
            'id': objet.id,
            'name': objet.name,
            'price': objet.price,
            'link': objet.link,
        }
        return JsonResponse(serialized_data)
    def post(self, request, *args, **kwargs):
        id = request.POST.get('id')
        name = request.POST.get('name')
        price = request.POST.get('price')
        link = request.POST.get('link')

        # Effectuer des opérations de création ou de mise à jour selon vos besoins
        objet, created = Sneaker.objects.get_or_create(id=id, name=name, price=price, link=link)
        return JsonResponse({'message': 'Opération réussie'})

    def delete(self, request, *args, **kwargs):
        id = kwargs.get('id')
        objet = get_object_or_404(Sneaker, id=id)
        objet.delete()
        return JsonResponse({'message': 'Objet supprimé'})

    def put(self, request, *args, **kwargs):
        id = kwargs.get('id')
        nouvel_attribut = request.POST.get('nouvel_attribut')
        objet = get_object_or_404(Sneaker, id=id)
        objet.attribut = nouvel_attribut
        objet.save()
        return JsonResponse({'message': 'Objet mis à jour'})