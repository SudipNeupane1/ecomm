"""ecomm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import home,contact_page,login_page,register_page
# logout_page
# from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from carts.views import cart_detail




urlpatterns = [
    path('',home,name='home'),
    path('contact/',contact_page,name='contact'),
    path('login/',login_page,name='login'),
    path('register/',register_page,name='register'),
   
    path('products/',include(("products.urls",'products'),namespace='products')),
    path('cart/',include(("carts.urls",'cart'),namespace = 'cart')),
    # path('logout/',Logoutview.as_view(),name='logout'),
    path('',include(('search.urls','search'),namespace ='search')),
    # path('',include('ecomm.urls',namespace = 'ecomm')),
     path('admin/', admin.site.urls),

    
]



if settings.DEBUG:
    urlpatterns  = urlpatterns + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns  = urlpatterns + static(settings.STATIC_URL,document_root=settings.MEDIA_ROOT)
