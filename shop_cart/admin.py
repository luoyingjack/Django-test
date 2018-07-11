from django.contrib import admin
import xadmin
# Register your models here.

from shop_cart.models import Cart, Product


class ProductAdmin(object):
    list_display = ['title', 'description', 'image_url', 'price', 'createtime']
    search_fields = ['title', 'description', 'image_url']
    list_filter = ['title', 'description', 'image_url', 'price', 'createtime']
    list_per_page = 2
    editable = ['title']


xadmin.site.register(Product, ProductAdmin)



