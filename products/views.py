
from django.views.generic import ListView,DetailView
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from carts.models import Cart 
from .models import Product,Category

class ProductListView(ListView):
    template_name = "products/list.html"


    def get_context_data(self,*args,**kwargs):
        context = super(ProductListView,self).get_context_data(*args,**kwargs)
        cart_obj,new_obj = Cart.objects.new_or_get(self.request)
        context['cart']=cart_obj
        return context

    def get_queryset(self,*args,**kwargs):
        request = self.request
        return Product.objects.all()
# def product_list_view(request):
#     queryset= Product.objects.all()
#     context = {
#         'objects_list':queryset

#     }
#     return render(request,"products/list.html",context)

def product_list(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Procuct.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {'category': category, 'categories': categories, 'products': products}
    return render(request, 'products/list.html', context)


    
class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"


    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context


    def get_object(self,*args,**kwargs):
        request = self.request
        slug = self.kwargs.get('slug')

        try:
            instance = Product.objects.get(slug=slug,available = True)
        except Product.DoesNotExist:
            raise Http404("NOt founc..")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug,available=True)
            instance = qs.first()
        except:
                raise Http404("Uhhmm")
        return instance




class ProductDetailView(DetailView):
    #queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        # context['abc'] = 123
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('slug')
        instance = Product.objects.get_by_id(slug)
        if instance is None:
            raise Http404("Product doesn't exist")
        return instance


def product_detail_view(request,slug=None,*args,**kwargs):
    instance = Product.objects.get_by_id(slug)
    if instance is None:
        raise Http404("Product doesn't exist")

    context = {
        'object':instance
    }
    return render(request,"products/detail.html",context)




