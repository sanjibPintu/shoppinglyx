from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import (
  Customer,
  Product,
  Cart,
  OrerPlaced
)

# Register your models here.
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
  list_display=[
    'id','user','name','city','zipcode','state' 
  ]
@admin.register(Product)  
class ProductModelAdmin(admin.ModelAdmin):
  list_display=['id','title','seeling_price','discount_price','brand','description','catagory','product_image']  

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
  list_display=[
    'id','user','product','product_info','quantity'
  ]
  def product_info(self,obj):
    link=reverse("admin:app_product_change",args=[
      obj.product.pk
    ])
    return format_html('<a href="{}">{}</a>',link,obj.product.title)

@admin.register(OrerPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
  list_display=[
    'id','user','customer','customer_info','product','product_info','quantity','order_date','status',
    'price'
  ]
  def customer_info(self,obj):
    link=reverse("admin:app_customer_change",args=[
      obj.customer.pk
    ])
    return format_html('<a href="{}">{}</a>',link,obj.customer.name)
  
  def product_info(self,obj):
    link=reverse("admin:app_product_change",args=[
      obj.product.pk
    ])
    return format_html('<a href="{}">{}</a>',link,obj.product.title)







