from django.contrib import admin
from .models import ProductModel,CategoryModel,CustomerModel

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(ProductModel,AdminProduct)
admin.site.register(CategoryModel)
admin.site.register(CustomerModel)
