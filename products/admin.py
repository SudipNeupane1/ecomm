from django.contrib import admin
from .models import Category,Product

# class CategoryAdmin(admin,ModelAdmin):
#     list_display = ['__str__', 'slug']
#     class Meta:
#         model =Categoty

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    class Meta:
        model = Product

# admin.site.register(Product, ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product ,ProductAdmin)