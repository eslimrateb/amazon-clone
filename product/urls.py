from .views import BrandList, ProductList, ProductDetail,BrandList
from django.urls import path


urlpatterns = [
    path("", ProductList.as_view()),
    path("brands/", BrandList.as_view()),
    path("<slug:slug>/", ProductDetail.as_view()),
    
]