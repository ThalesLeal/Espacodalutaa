# coding=utf-8

from django.shortcuts import render,get_object_or_404

from .models import Product, Category


def product_list(request):
    context = {
        'product_list': Product.objects.all()
    }
    return render(request, 'catalog/product_list.html', context)


def category(request, slug):
    category = Category.objects.get(slug=slug)
    context = {
        'current_category': category,
        'product_list': Product.objects.filter(category=category),
    }
    return render(request, 'catalog/category.html', context)


def product(request, slug):
    product = Product.objects.filter(slug=slug)
    context = {
        'current_product': product,
        # 'product_list': Product.objects.filter(slug=product),
        }
    return render(request, 'catalog/product.html', context)
