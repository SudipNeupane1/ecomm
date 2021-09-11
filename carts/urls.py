# from djnago.conf.urls import  path
from .import views
from django.urls import path

from .views import (
    cart_home,
    cart_update,

)
app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('<int:product_id>/', views.cart_home,name='cart_home'),
    path('<int:product_id>/', views.cart_update, name='cart_update'),
]