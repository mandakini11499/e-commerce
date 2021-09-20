from django.shortcuts import render, redirect
from store.models import CustomerModel
from django.contrib.auth.hashers import make_password
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, "signup.html")

    def post(self, request):
        postData = request.POST
        first_name = postData.get('fname')
        last_name = postData.get('lname')
        phone_no = postData.get('phone')
        email = postData.get('email')
        pwd = postData.get('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone_no': phone_no,
            'email': email
        }
        customer = CustomerModel(first_name=first_name,
                                 last_name=last_name,
                                 phone_number=phone_no,
                                 email=email,
                                 password=pwd)

        error_message = self.validateCustomer(customer)
        # saving
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            return render(request, 'signup.html', {'error': error_message, 'values': value})

    def validateCustomer(self, cust):
        error_message = None
        if (not cust.first_name):
            error_message = "First_name Required!!"
        elif len(cust.first_name) < 4:
            error_message = "First_name must be 4 char long or more"
        elif (not cust.last_name):
            error_message = "Last_name Required!!"
        elif len(cust.last_name) < 4:
            error_message = "Last_name must be 4 char long or more"
        elif not cust.phone_number:
            error_message = "Phone number Required!!"
        elif len(cust.phone_number) < 10:
            error_message = "Phone number must be 10 Integers long"
        elif not cust.password:
            error_message = "Password Required"
        elif len(cust.password) < 10:
            error_message = "Password must be 8 char long or more"
        elif not cust.email:
            error_message = "Email field Required"
        elif len(cust.email) < 5:
            error_message = "email must be 10 char long or more"
        elif cust.isExists():
            error_message = "Email Address Already Exists"
        return error_message
