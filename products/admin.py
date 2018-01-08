from django.contrib import admin
from .models import ProductsWarehouse, CellsWarehouse, Storage


# Register your models here.

admin.site.register(ProductsWarehouse)
admin.site.register(CellsWarehouse)
admin.site.register(Storage)