from django.contrib import admin
from .models import Product, Material, ProductMaterial, Warehouses


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_code')
    search_fields = ('product_name', 'product_code')


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('material_name',)
    search_fields = ('material_name',)


class ProductMaterialAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'material_id', 'quantity')
    search_fields = ('product_id', )


class WarehousesAdmin(admin.ModelAdmin):
    list_display = ('material_id', 'remainder', 'price')
    search_fields = ('material_id', )


admin.site.register(Product, ProductAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(ProductMaterial, ProductMaterialAdmin)
admin.site.register(Warehouses, WarehousesAdmin)
