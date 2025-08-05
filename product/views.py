from statistics import quantiles
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Q ,F ,Value
from .models import Product, ProductImages, Brand, Review
from django.db.models.aggregates import Min ,Max, Avg , Count



def queryset_debug(request):

    # data=Product.objects.select_related('brand')  #foreng key relations and one-to-one
    # data = data.prefetch_related('brand').all()  # prefetch_related for many-to-many or reverse foreign key relations
    #filter
    # data=Product.objects.filter(price__gt=20)
    # data=Product.objects.filter(price__gte=20)
    # data=Product.objects.filter(price__lt=20)
    # data=Product.objects.filter(price__lte=20)
    # data=Product.objects.filter(price__range=(15,20))
    # navigaion relation 
    # data=Product.objects.filter(brand__name='apple',quantity__gt=8)#and
    # data=Product.objects.filter(Q(brand__name='apple')|Q(quantity__gt=56))#or
    # data=Product.objects.filter(price=F('quantity'))
    # data=Product.objects.order_by('name')
    # data=Product.objects.values_list('name','price')
    # data=Product.objects.values('name','price')
    # data=Product.objects.distinct()
    # data=Product.objects.defer('slug')
    # data=Product.objects.aggregate(Max('quantity'))
    # add new field form cal
    data=Product.objects.annotate(price_e=F('price')*300)


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
    queryset=Brand.objects.annotate(product_count=Count('product_brand'))



class BrandDetail(ListView):
    model = Product
    template_name = 'product/brand_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"]=Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count=Count('product_brand'))[0]
        return context
    
    def get_queryset(self):
        brand=Brand.objects.get(slug=self.kwargs['slug'])
        return super().get_queryset().filter(brand=brand)
