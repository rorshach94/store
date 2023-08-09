from django.contrib import admin
from . models import Customer, Product

@admin.register(Product)
# Register your models here.
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','discounted_price','category','product_image']

@admin.register(Customer)
# Register your models here.
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','locality','city','state','zipcode']