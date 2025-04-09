from django.contrib import admin
from shop.models import *
# Register your models here.

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)