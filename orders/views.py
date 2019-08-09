from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Pizza, Topping, Sub, Pasta, Salad, Dinner_Platter, Pizza_Order, Sub_Order, Order

# Create your views here.
def index(request):
	if not request.user.is_authenticated:
		return render(request, "orders/login.html", {"message": None})

	context = {
		"pizzas": Pizza.objects.all(),
		"user": request.user,
		"toppings": Topping.objects.all(),
		"subs": Sub.objects.all(),
		"pastas": Pasta.objects.all(),
		"salads": Salad.objects.all(),
		"dinner_platters": Dinner_Platter.objects.all()
	}
	return render(request, "orders/index.html", context)

def login_view(request):
	username = request.POST["username"]
	password = request.POST["password"]
	user = authenticate(request, username=username, password=password)

	if user is not None:
		login(request, user)
		return HttpResponseRedirect(reverse("index"))
	else:
		return render(request, "orders/login.html", {"message": "Invalid Login Credentials"})

def logout_view(request):
	logout(request)
	return render(request, "orders/login.html", {"message": "Logged Out"})

def register(request):
	return render(request, "orders/register.html")

def new_user(request):
	username = request.POST["uname"]
	password = request.POST["pass"]
	email = request.POST["email"]
	fname = request.POST["fname"]
	lname = request.POST["lname"]

	try:
		user=User.objects.create_user(username, email, password)
		user.first_name = fname
		user.last_name = lname
		user.save()
	except:
		return render(request, "orders/login.html", {"message": "Error creating new user, username already taken"})

	return render(request, "orders/login.html", {"message": "Successfully created new user!"})

def new_item(request):
	price = request.POST["price"]
	toppings = request.POST.getlist("toppings")
	item = request.POST["new"]
	pk = request.POST["pk"]
	user = request.user.username
	try:
		order = Order.objects.get(user=user, final=False)
	except:
		order = Order(user=user, total=0)
		order.save()

	if item=="pizza":
		toppings = request.POST.getlist("toppings")
		p = Pizza.objects.get(pk=pk)
		po = Pizza_Order(pizza=p, user=user)
		po.save()
		for t in toppings:
			top = Topping.objects.get(topping=t)
			po.toppings.add(top)
		order.pizza_orders.add(po)


	elif item=="sub":
		extras = request.POST.getlist("extra")
		s = Sub.objects.get(pk=pk)
		so = Sub_Order(sub=s, user=user)
		so.save()
		for x in extras:
			setattr(so, x, True)
			so.save()
		order.sub_orders.add(so)

	elif item=="pasta":
		p = Pasta.objects.get(pk=pk)
		order.pastas.add(p)

	elif item=="salad":
		s = Salad.objects.get(pk=pk)
		order.salads.add(s)

	else:
		dp = Dinner_Platter.objects.get(pk=pk)
		order.dinner_platters.add(dp)

	order.total = order.total + float(price)
	order.save()
	return HttpResponse(price)
