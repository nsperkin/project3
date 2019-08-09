from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_user", views.new_user, name="new_user"),
    path("new_item", views.new_item, name="new_item"),
    path("cart", views.cart, name="cart"),
    path("submit", views.submit, name="submit")
]
