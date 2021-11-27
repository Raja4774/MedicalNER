from django.db import models


class MedicineModel(models.Model):
    sku_id = models.CharField(max_length=25, null=True, blank=True)
    product_id = models.CharField(max_length=25, null=True, blank=True)
    sku_name = models.CharField(max_length=100, null=True, blank=True)
    price = models.CharField(max_length=25, null=True, blank=True)
    manufacturer_name = models.CharField(max_length=100, null=True, blank=True)
    salt_name = models.TextField(null=True, blank=True)
    drug_form = models.CharField(max_length=50, null=True, blank=True)
    Pack_size = models.CharField(max_length=50, null=True, blank=True)
    strength = models.TextField(null=True, blank=True)
    product_banned_flag = models.CharField(
        max_length=10, null=True, blank=True)
    unit = models.CharField(max_length=50, null=True, blank=True)
    price_per_unit = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = "medicine"
