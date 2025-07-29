from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Product, ProductImages, Brand, Review

class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product
