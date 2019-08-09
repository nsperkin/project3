from django.db import models

# Create your models here.
class Topping(models.Model):
	topping = models.CharField(max_length=64)

	def __str__(self):
		return self.topping

class Pizza(models.Model):
	class Meta:
		ordering=['style']
		
	style = models.CharField(max_length=64)
	size = models.CharField(max_length=64)
	num_toppings = models.IntegerField()
	price = models.FloatField()

	def __str__(self):
		return f"{self.size} {self.style} Pizza with {self.num_toppings} toppings: ${self.price:.2f}"

class Pizza_Order(models.Model):
	pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
	toppings = models.ManyToManyField(Topping, blank=True)
	user = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.pizza}"

class Sub(models.Model):
	style = models.CharField(max_length=64)
	price = models.FloatField()
	size = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.size} {self.style} sub: ${self.price:.2f}"

class Sub_Order(models.Model):
	sub = models.ForeignKey(Sub, on_delete=models.CASCADE)
	extra_cheese = models.BooleanField(default=False)
	extra_muchrooms = models.BooleanField(default=False)
	extra_green_peppers = models.BooleanField(default=False)
	extra_onions = models.BooleanField(default=False)
	user = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.sub}"

class Pasta(models.Model):
	pasta = models.CharField(max_length=64)
	price = models.FloatField()

	def __str__(self):
		return f"{self.pasta} pasta: ${self.price}"

class Salad(models.Model):
	salad = models.CharField(max_length=64)
	price = models.FloatField()

	def __str__(self):
		return f"{self.salad}: ${self.price}"

class Dinner_Platter(models.Model):
	dinner_platter = models.CharField(max_length=64)
	price = models.FloatField()
	size = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.size} {self.dinner_platter}: ${self.price}"

class Order(models.Model):
	pizza_orders = models.ManyToManyField(Pizza_Order, blank=True)
	sub_orders = models.ManyToManyField(Sub_Order, blank=True)
	pastas = models.ManyToManyField(Pasta, blank=True)
	salads = models.ManyToManyField(Salad, blank=True)
	dinner_platters = models.ManyToManyField(Dinner_Platter, blank=True)
	total = models.FloatField()
	user = models.CharField(max_length=64)
	final = models.BooleanField(default=False)