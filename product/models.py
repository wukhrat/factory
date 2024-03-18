from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='mahsulot nomi')
    product_code = models.IntegerField(verbose_name='mahsulot kodi')

    def __str__(self):
        return f'{self.product_name}  {self.product_code}'


class Material(models.Model):
    material_name = models.CharField(max_length=100, verbose_name='homashiyo nomi')

    def __str__(self):
        return f'{self.material_name}'


class ProductMaterial(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    material_id = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='material soni')


class Warehouses(models.Model):
    material_id = models.ForeignKey(Material, on_delete=models.CASCADE)
    remainder = models.IntegerField(verbose_name='qolgan homashiyo soni')
    price = models.FloatField(verbose_name='narx')
