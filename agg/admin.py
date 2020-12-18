from django.contrib import admin

# Register your models here.
from agg.models import Product_Log, Product

admin.site.register(Product)
admin.site.register(Product_Log)