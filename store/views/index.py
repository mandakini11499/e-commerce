from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.models import ProductModel,CategoryModel
from django.views import View


class Index(View):
   def post(self,request):
      product=request.POST.get('product')
      print(product)
      cart=request.session.get('cart')
      if cart:
         quantity=cart.get(product)
         if quantity:
            cart[product]= quantity+1
         else:
            cart[product]=1
      else:
         cart={}
         cart[product] = 1
      request.session['cart']=cart
      print(request.session['cart'])
      return redirect('homepage')

   def get(self,request):
      cart=request.session.get('cart')
      if not cart:
         request.session.cart={}
      products=None
      #request.session.clear()
      category = CategoryModel.get_all_categories()
      categoryId = request.GET.get('category')
      if categoryId:
         products = ProductModel.get_all_products_by_categoryid(categoryId)
      else:
         products = ProductModel.get_all_products()
      data = {}
      data['products'] = products
      data['category'] = category
      print('you are :', request.session.get('email'))
      return render(request, "index.html", data)



