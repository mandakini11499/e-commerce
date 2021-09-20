from django.shortcuts import render,redirect
from store.models import CustomerModel
from django.contrib.auth.hashers import check_password
from django.views import View

class Login(View):
    def get(self,request):
        return render(request, "login.html")
    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = CustomerModel.get_customer_by_email(email)
        error_message = None
        if customer:
            pwd = check_password(password, customer.password)
            if pwd:
                request.session['customer_id']=customer.id
                request.session['email']=customer.email
                return redirect('homepage')
            else:
                error_message = "Email or Password Invalid"
        else:
            error_message = "Email or Password Invalid"

        return render(request, 'login.html', {'error': error_message})