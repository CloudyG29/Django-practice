from django.contrib import admin


# Register your models here.
from .models import Product,Stock

admin.site.register(Product)
admin.site.register(Stock)