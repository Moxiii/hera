from django.urls import path , include
from api.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Sneaker',SneakerViewSet)


urlpatterns = [
    path('/',include(router.urls) ),
    path('/objet/<int:id>/', GestionObjetView.as_view(), name='gestion_objet'),
]
