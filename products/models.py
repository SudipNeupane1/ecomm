from django.db import models
import random
import os
from django.db.models import Q
from django.db.models.signals import pre_save,post_save
from django.urls import reverse
from ecomm.utils import unique_slug_generator




class Category(models.Model):
    name = models.CharField(max_length = 200,db_index = True)
    slug = models.SlugField(max_length =200,unique =True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("products:product_list_by_category",kwargs ={"slug": self.slug})





def get_filename_ext(filepath):
    base_name =os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance,filename):
    new_filename = random.randint(1,3910209312)
    name,ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
    return "products/{new_filename}/{final_filename}".format(
            new_filename=new_filename,
            final_filename=final_filename
    )
class ProductQuerySet(models.query.QuerySet):

    def available(self):
        return self.filter(available=True)
    def featured(self):
        return self.filter(featured=True,available=True)
    
    def search(self,query):
        lookups = (Q(title_icontains=query)|
                  Q(description_icontains=query)|
                  Q(price_icontains=query) |
                  Q(tag_title_icontains=query)
        )
        return self.filter(lookups).distinct()
class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)
        
    def all(self):
        return self.get_queryset().available()
        
    def featured(self):
        return self.get_queryset().featured()
    
    def get_by_id(self,id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() ==1:
            return qs.first()
        return None

    # def search(self,query):
    #     return self.get_queryset().activate().search(query)
    
class Product(models.Model):
    category    = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)

    title       = models.CharField(max_length = 120)
    slug        = models.SlugField(max_length =200,unique =True)
    description = models.TextField()
    price       = models.DecimalField(decimal_places=2,max_digits=20,default=199.99)
    image       = models.ImageField(upload_to=upload_image_path,null=True,blank=True)
    featured    = models.BooleanField(default=False)
    available     = models.BooleanField(default=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects =ProductManager()

    def get_absolute_url(self):
        return reverse("products:list",kwargs ={"slug": self.slug})

    def __str__(self):
        return self.title 
    def __unicode__(self):
        return self.title 
    
    @property
    def name(self):
        return self.title
def product_pre_save_receive(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

    pre_save.connect(product_pre_save_receiver,sender=Product)









