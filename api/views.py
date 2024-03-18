from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers import WarehousesSerializer, ProductMaterialSerializer
from product.models import Warehouses, ProductMaterial


class WarehousesApiView(APIView):
    def get(self, request):

        result = []

        # Retrieve all warehouses
        warehouses = Warehouses.objects.all()

        for warehouse in warehouses:
            warehouse_data = WarehousesSerializer(warehouse).data
            products = []

            # Retrieve products related to the warehouse
            products_materials = ProductMaterial.objects.all()
            for product_material in products_materials:
                product_material_data = ProductMaterialSerializer(product_material).data.get('product_name')
                products.append(product_material_data)

            warehouse_data['product_materials'] = products
            result.append({'result': warehouse_data})

        return Response(result)

