from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Pizza

# Create your views here.
def index(request):
	if not request.user.is_authenticated:
		return render(request, "orders/login.html", {"message": None})

	context = {
		"pizza": Pizza.objects.all(),
		"user": request.user
	}
	return render(request, "orders/login.html", {"message": None})
	#return render(request, "orders/index.html", context)

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