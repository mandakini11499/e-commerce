from django.db import models

class CustomerModel(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone_number=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=50)

    def register(self):
        return self.save()
    @staticmethod
    def get_customer_by_email(email):
        try:
           return CustomerModel.objects.get(email=email)
        except:
            return False



    def isExists(self):
        if CustomerModel.objects.filter(email=self.email):
            return True
        return False