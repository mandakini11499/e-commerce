from django.db import models
from .category import CategoryModel


class ProductModel(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    description=models.CharField(max_length=100,default='')
    image=models.ImageField(upload_to='uploads/product/')
    category=models.ForeignKey(CategoryModel,default=1,on_delete=models.CASCADE)

    @staticmethod
    def get_all_products():
        return ProductModel.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
             return ProductModel.objects.filter(category=category_id)
        else:
            return ProductModel.get_all_products()
    




