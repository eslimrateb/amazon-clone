from .views import BrandDetail, BrandList, ProductList, ProductDetail,BrandDetail,queryset_debug
from django.urls import path


urlpatterns = [
    path("", ProductList.as_view()),
    path("debug",queryset_debug),
    path("brands/", BrandList.as_view()),
    path("<slug:slug>/", ProductDetail.as_view()),
    path("brands/<slug:slug>/", BrandDetail.as_view()),

]