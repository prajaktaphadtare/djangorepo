from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    barcode = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField()

    class Meta:
        db_table = "product_info"

class Vendor(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        db_table = "vendor_info"
