from django.contrib import admin
from .models import Product, Material, ProductMaterial, Warehouses


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_code')
    search_fields = ('product_name', 'product_code')


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('material_name',)
    search_fields = ('material_name',)


class ProductMaterialAdmin(admin.ModelAdmin):
    list_display = ()
    search_fields = ()


class WerehousesAdmin(admin.ModelAdmin):
    list_display = ()
    search_fields = ()


admin.site.register(Product, ProductAdmin)
admin.site.register(Material, MaterialAdmin)
