from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Product, ProductImages, Brand, Review

class ProductList(ListView):
    model = Product

class ProductDetail(DetailView):
    model = Product
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.filter(product=self.object)
        context['related_products'] = Product.objects.filter(brand=self.object.brand).exclude(id=self.object.id)
        return context
    
class BrandList(ListView):
    model = Brand
