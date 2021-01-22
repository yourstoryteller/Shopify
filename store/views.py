from xhtml2pdf import pisa
from django.views import View
from django.db import transaction
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.template.loader import get_template
from .models import Product, Discount, Order
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignUpView(View):
    def get(self, request):
        # Display Signup form
        form = UserCreationForm
        data = {'form': form}

        return render(request, 'signup.html', data)

    def post(self, request):
        # Get data from filled form and create account if data is valid
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/')

        data = {'form': form}

        return render(request, 'signup.html', data)


class LoginView(View):
    return_url = None

    def get(self, request):
        # Display Login form
        LoginView.return_url = request.GET.get('next')
        form = AuthenticationForm
        data = {'form': form}

        return render(request, 'login.html', data)

    def post(self, request):
        # Get data from filled form and login user if data is valid
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # If return url exists then navigate user back to return url after logging
            if (LoginView.return_url) and (LoginView.return_url != '/invoice'):
                url = LoginView.return_url
                return HttpResponseRedirect(url)
            else:
                LoginView.return_url = None
                if user.is_staff == True:
                    return HttpResponseRedirect('/admin')
                return HttpResponseRedirect('/')

        data = {'form': form}

        return render(request, 'login.html', data)


class LogoutView(View):
    # Logout user
    def get(self, request):
        logout(request)

        return HttpResponseRedirect('/')


class IndexView(View):
    return_url = None

    def get(self, request):
        IndexView.return_url = request.GET.get('page')
        cart = request.session.get('cart')

        # Update discount on products on homepage
        Discount.update_discount()

        # Create cart for user if not created already
        if not cart:
            request.session['cart'] = {}

        # Display all products and paginate them
        products = Product.get_all_products()
        paginator = Paginator(products, per_page=6)
        page_num = request.GET.get('page', 1)
        products = paginator.get_page(page_num)

        data = {'products': products, 'paginator': paginator, 'page_num': int(page_num)}

        return render(request, 'index.html', data)

    def post(self, request):
        # Add or remove cart items
        product = request.POST.get('product_id')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')

        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {product: 1}

        # Update cart
        request.session['cart'] = cart

        # Navigate user to recently accessed product's page
        if IndexView.return_url:
            url = '?page=' + IndexView.return_url
            return HttpResponseRedirect(url)
        else:
            IndexView.return_url = None

        return redirect('store:index')


class CartView(View):
    def get(self, request):
        # Display cart
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)

        data = {'products': products}

        return render(request, 'cart.html', data)


class CheckoutView(View):
    def get(self, request):
        # Redirect to homepage if GET request is received
        return redirect('store:index')

    @transaction.atomic
    def post(self, request):
        # Create order and update order table (1 Order : 1 Product)
        user = request.user
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))

        for product in products:
            if product.disc_price is not None:
                price = product.disc_price
            else:
                price = product.price
            quantity = cart.get(str(product.id))

            order = Order(user=user, product=product, price=price, quantity=quantity)
            order.save()

            # Send POST request to invoice view
            return InvoiceView.post(self, request)


class InvoiceView(View):
    def get(self, request):
        # Redirect to homepage if GET request is received
        return redirect('store:index')

    def post(self, request):
        # Add cart to invoice and empty cart
        cart = request.session['cart']

        # Create invoice PDF and download automatically on user's setup
        ids = list(cart.keys())
        products = Product.get_products_by_id(ids)
        base_url = request.get_host
        data = {'products': products, 'request': request, 'base_url': base_url}
        template = get_template('invoice.html')
        html = template.render(data)
        file = open('invoice.pdf', "w+b")
        pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file, encoding='utf-8')
        file.seek(0)
        pdf = file.read()
        file.close()
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = request.user.username + "-invoice.pdf"
            content = "attachment; filename=%s" % filename
            response['Content-Disposition'] = content
            request.session['cart'] = {}
            return response
        return HttpResponse("Error occurred while generating invoice.")


class OrdersView(View):
    def get(self, request):
        # Display all orders of user and paginate them
        orders = Order.get_orders_by_user(request.user)
        paginator = Paginator(orders, per_page=4)
        page_num = request.GET.get('page', 1)
        orders = paginator.get_page(page_num)

        data = {'orders': orders, 'paginator': paginator, 'page_num': int(page_num)}

        return render(request, 'orders.html', data)
