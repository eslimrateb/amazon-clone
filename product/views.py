from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Product, ProductImages, Brand, Review

class ProductList(ListView):
    model = Product

class ProductDetail(DetailView):
    model = Product
