from django.contrib import admin

from .models import Pizza, Pizza_Order, Topping, Sub, Sub_Order, Pasta, Salad, Dinner_Platter, Order
# Register your models here.
l = [Pizza, Pizza_Order, Topping, Sub, Sub_Order, Pasta, Salad, Dinner_Platter, Order]

for item in l:
	admin.site.register(item)