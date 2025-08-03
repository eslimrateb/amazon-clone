from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Product, ProductImages, Brand, Review




def queryset_debug(request):

    data=Product.objects.select_related('brand').all
    
    return render(request, 'product/debug.html',{"data":data})


class ProductList(ListView):
    model = Product

class ProductDetail(DetailView):
    model = Product
    def get_context_data(self, **kwargs): # v:r
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.filter(product=self.object)
        context['related_products'] = Product.objects.filter(brand=self.object.brand).exclude(id=self.object.id)
        return context
    
class BrandList(ListView):
    model = Brand

class BrandDetail(ListView):
    model = Product
    template_name = 'product/brand_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"]=Brand.objects.get(slug=self.kwargs['slug'])
        return context
    
    def get_queryset(self):
        brand=Brand.objects.get(slug=self.kwargs['slug'])
        return super().get_queryset().filter(brand=brand)
