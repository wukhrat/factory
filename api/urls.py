# urls.py
from django.urls import path

from api.views import WarehousesApiView

app_name = 'api'
urlpatterns = [
    path('warehouses/', WarehousesApiView.as_view(), name='warehouse-api'),
]
