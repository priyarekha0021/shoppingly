from django.contrib import admin
from .models import (
 Customer,
 Product,
 Cart,
 OrderPlaced
)

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
 list_display = ('id', 'user', 'name', 'locality', 'city','zipcode','state')

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
 list_display = ('id','title','selling_price','discounted_price','description','brand','category','product_image')
 def display_product_image(self, obj):
      return mark_safe(f'<img src="{obj.product_image.url}" width="50" height="50" />')

 display_product_image.short_description = 'Product Image'

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
 list_display = ('id','user','product','quantity')

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
 list_display = ('id','user','customer','product','quantity','ordered_date','status')

# #  def get_ordered_date(self, obj):
# #         return obj.ordered_date

# #  get_ordered_date.short_description = 'Ordered Date'









