from django.db import models


class Ven(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    class Meta:
        db_table = "ven_info"


class RainySeason(models.Model):
    name = models.CharField(max_length=50)
    barcode = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField()
    vendors = models.ManyToManyField(Ven)

    class Meta:
        db_table = "cloths_info"