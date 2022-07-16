from itertools import product
from math import prod
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import CategoryForm, ProductForm
from store.models import Category, Product

@login_required(login_url='/access/')
def crud(request):
    if request.user.role not in ('A'):
        messages.error(request, 'Acceso sólo para empleados y administradores.', extra_tags='danger')
        return redirect('/perfil/')
    return render(request, 'crud.html')

@login_required(login_url='/access/')
def create_category(request):
    if request.user.role not in ('A'):
        messages.error(request, 'Acceso sólo para empleados y administradores.', extra_tags='danger')
        return redirect('/perfil/')
    form = CategoryForm()
    if (request.method == 'POST'):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    context = {
        'section': 'category.registrar',
        'form': form,
        'estados': {
            'A': 'Active',
            'I': 'Inactive',
        }
    }
    return render(request, 'categories/create_category.html', context)

@login_required(login_url='/access/')
def categories(request):
    if request.user.role not in ('A'):
        messages.error(request, 'Acceso sólo para empleados y administradores.', extra_tags='danger')
        return redirect('/perfil/')
    categories = Category.objects.all()
    context = {
        'section': 'categories',
        'categories': categories,
        'estados': {
            'A': 'Active',
            'I': 'Inactive',
        }
    }
    return render(request, 'categories/categories.html', context)


def update_category(request,id):
    category = Category.objects.get(id = id)

    datos ={
        'form': CategoryForm(instance= category)
    }
    if request.method == 'POST': 
        formulario = CategoryForm(request.POST, instance = category)
        if formulario.is_valid: 
            formulario.save()           #permite actualizar la info del objeto encontrado
            return redirect('categories')
    return render(request, 'categories/update_category.html', datos)

@login_required(login_url='/access/')
def delete_category (request, id):
    instance = Category.objects.get(id=id)
    instance.delete()
    return redirect('categories')










#####
##
@login_required(login_url='/access/')
def create_product(request):
    if request.user.role not in ('A'):
        messages.error(request, 'Acceso sólo para empleados y administradores.', extra_tags='danger')
        return redirect('/perfil/')
    form = ProductForm()
    if (request.method == 'POST'):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')
    context = {
        'section': 'product.registrar',
        'form': form,
        'estados': {
            'A': 'Active',
            'I': 'Inactive',
        }
    }
    return render(request, 'products/create_product.html', context)

@login_required(login_url='/access/')
def products(request):
    if request.user.role not in ('A'):
        messages.error(request, 'Acceso sólo para empleados y administradores.', extra_tags='danger')
        return redirect('/perfil/')
    products = Product.objects.all()
    context = {
        'section': 'products',
        'products': products,
        'estados': {
            'A': 'Active',
            'I': 'Inactive',
        }
    }
    return render(request, 'products/products.html', context)


def update_product(request,id):
    product = Product.objects.get(id = id)

    datos ={
        'form': ProductForm(instance= product)
    }
    if request.method == 'POST': 
        formulario = ProductForm(request.POST,request.FILES, instance = product)
        if formulario.is_valid: 
            formulario.save()           #permite actualizar la info del objeto encontrado
            return redirect('products')
    return render(request, 'products/update_product.html', datos)

@login_required(login_url='/access/')
def delete_product(request, id):
    instance = Product.objects.get(id=id)
    instance.delete()
    return redirect('products')

    