from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup, name="signup"),
    path("get_price", views.get_price, name="get_price"),
    path("add2cart", views.add2cart, name="add2cart"),
    path("clear_cart", views.clear_cart, name="clear_cart"),
    path("checkout", views.checkout, name="checkout"),
    path("order", views.place_order, name="place_order"),
    path("order_view", views.order_view, name="order_view"),
    path("order_details/<int:order_id>", views.order_details, name="order_details"),
    path("change_order_status", views.change_order_status, name="change_order_status"),
    path("customer_order_view", views.customer_order_view, name="customer_order_view")
]
