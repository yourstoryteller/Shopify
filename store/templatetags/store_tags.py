from django import template

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False


@register.filter(name='get_product_quantity')
def get_product_quantity(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0;


@register.filter(name='cal_product_price')
def cal_product_price(product  , cart):
    if product.disc_price is not None:
        return product.disc_price * get_product_quantity(product, cart)
    return product.price * get_product_quantity(product, cart)


@register.filter(name='cal_cart_price')
def cal_cart_price(products, cart):
    price = 0
    for product in products:
        price += cal_product_price(product , cart)
    return price


@register.filter(name='currency')
def currency(price):
    return "₹ "+str(price)


@register.filter(name='multiply')
def multiply(num1 , num2):
    return num1 * num2