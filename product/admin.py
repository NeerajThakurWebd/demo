from django.contrib import admin
from product.models import Product


class ProductAdmin(admin.ModelAdmin):
      list_display=('product_image','product_name','product_des','product_prize')


admin.site.register(Product,ProductAdmin)
# Register your models here.
