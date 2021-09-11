from django.urls import path
from .views import (
        ProductListView,
        ProductDetailSlugView,
)
from . import views



urlpatterns = [
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<slug:list>/',ProductListView.as_view(), name='product_list'),
    path('<slug:detail_slug>/', ProductDetailSlugView.as_view(), name='product_detail_view'),
]
                      
