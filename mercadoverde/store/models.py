from django.db import models
from django.contrib.auth.models import AbstractUser

class Category(models.Model):
    name = models.CharField(max_length = 80)
    status = models.CharField(max_length = 1, choices=[('1', 'Active'), ('0', 'Inactive')], default='A')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 80)
    description = models.TextField()
    stock = models.IntegerField(default = 0)
    money = models.CharField(max_length = 3, default = 'CLP')
    price = models.IntegerField()
    order_price = models.DecimalField(max_digits = 6, decimal_places = 0)
    image = models.ImageField(null = True, upload_to = 'media')
    status = models.CharField(max_length = 1, choices=[('1', 'Active'), ('0', 'Inactive')], default='A')
    category = models.ForeignKey('Category', on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class Order(models.Model):
    date = models.DateTimeField(auto_now_add = True)
    amount = models.IntegerField()
    status = models.CharField(max_length=1, choices=[('E', 'Entered'), ('C', 'Cancelled'), ('A', 'Accepted')], default='E')

    def __str__(self):
        return 'Order #' + str(self.id)

class Shopping(models.Model):
    date = models.DateTimeField(auto_now_add = True)
    amount = models.IntegerField()
    status = models.CharField(max_length=1, choices=[('1', 'Processing'), ('2', 'Underway'), ('3', 'Delivered')], default='1')
    user = models.ForeignKey('User', on_delete = models.CASCADE)
    tin = models.CharField(max_length = 12)
    adress = models.ForeignKey('Adress', on_delete = models.CASCADE)
    phone_number =models.CharField(max_length = 12, blank = True)

    def __str__(self):
        return 'Shopping #' + str(self.id)

class Detail(models.Model):
    units = models.IntegerField()
    amount = models.IntegerField()
    shopping = models.ForeignKey('Shopping', on_delete = models.CASCADE)
    order = models.ForeignKey('Order', on_delete = models.CASCADE)
    product = models.ForeignKey('Product', on_delete = models.CASCADE)

    def __str__(self):
        return ('Shipping #' + str(self.shopping.id))

class User(AbstractUser):
    email = models.EmailField(unique = True)
    role = models.CharField(max_length = 1, choices = [('C', 'Client'), ('A', 'Administrator')], default = 'C')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Adress(models.Model):
    place = models.CharField(max_length = 50)
    adress = models.CharField(max_length = 50)
    reference = models.TextField(blank = True)
    user = models.ForeignKey('User', on_delete = models.CASCADE)

    def __str__(self):
        return', '.join([self.place, self.adress, self.reference])