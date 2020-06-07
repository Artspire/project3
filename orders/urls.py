from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("menu", views.menu, name="menu"),
    path("add", views.add, name="add"),
    path("cart", views.cart, name="cart"),
    path("history", views.history, name="history"),
    path("manager", views.manager, name="manager")
]
