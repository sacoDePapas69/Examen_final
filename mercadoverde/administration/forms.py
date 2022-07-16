from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from store.models import Product, Category

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'status']

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'stock', 'money', 'price', 'order_price', 'image', 'status', 'category']

