from django.shortcuts import render
from rest_framework import viewsets
from api.models import Sneaker
from api.serializers import SneakerSerializer
# Create your views here.
class SneakerViewSet(viewsets.ModelViewSet):
    queryset = Sneaker.objects.all()
    serializer_class=SneakerSerializer