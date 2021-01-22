from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import SignUpView, LoginView, LogoutView, IndexView, CartView, CheckoutView, OrdersView, InvoiceView

app_name = 'store'
urlpatterns = [
    path('signup', SignUpView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),

    path('', IndexView.as_view(), name='index'),
    path('cart', CartView.as_view(), name='cart'),
    path('checkout', login_required(CheckoutView.as_view()), name='checkout'),
    path('invoice', login_required(InvoiceView.as_view()), name='invoice'),
    path('orders', login_required(OrdersView.as_view()), name='orders')

]
