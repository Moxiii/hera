from rest_framework import serializers
from api.models import Sneaker

class SneakerSerializer(serializers.HyperlinkedModelSerializer):
    """Serializes a sneakers object."""
    class Meta:
        model = Sneaker
        fields = ['id','name','price','link']