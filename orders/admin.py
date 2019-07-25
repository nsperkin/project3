from django.contrib import admin

from .models import Pizza, Pizza_Order, Topping, Sub, Sub_Order, Pasta, Salad, Dinner_Platter
# Register your models here.
l = [Pizza, Topping, Sub, Sub_Order, Pasta, Salad, Dinner_Platter]

for item in l:
	admin.site.register(item)