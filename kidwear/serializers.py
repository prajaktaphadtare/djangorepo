from rest_framework.serializers import ModelSerializer
from kidwear.models import *

class VenSer(ModelSerializer):
    class Meta:
        model = Ven
        fields = '__all__'

class RainySeasonSer(ModelSerializer):
    class Meta:
        model = RainySeason
        fields = '__all__'