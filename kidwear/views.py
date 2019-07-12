from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from kidwear.models import *
from kidwear.serializers import *

class VenVset(ModelViewSet):
    queryset =  Ven.objects.all()
    serializer_class = VenSer

class RainySeasonVset(ModelViewSet):
    queryset = RainySeason.objects.all()
    serializer_class = RainySeasonSer
