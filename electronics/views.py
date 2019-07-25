from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from electronics.models import *
from electronics.serializers import*

class ProductsVset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSer

print("hi, this is electonic.views")


class VendorVset(ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSer

