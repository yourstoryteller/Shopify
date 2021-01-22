from django.db import models
from django.utils.timezone import now
from datetime import date
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# ------------------------------------------------------------------
# PRODUCT MODEL
# ------------------------------------------------------------------

class Product(models.Model):
    def update_image_path(instance, filename):
        name = str(instance.name)
        path = 'uploads/products/' + name.replace(" ", "-") + '.' + filename.split(".")[-1]
        return path

    def update_description(self):
        return 'This is ' + str(self.name) + '.'

    # --------------------------------------------------------------

    name = models.CharField(max_length=60, unique=True)
    price = models.IntegerField()
    disc_price = models.IntegerField(editable=False, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to=update_image_path)

    class Meta:
        ordering = ['id']

    # --------------------------------------------------------------

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.description is None:
            self.description = self.update_description()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image.delete()
        super(Product, self).delete(*args, **kwargs)

    @staticmethod
    def get_product_by_id(id):
        return Product.objects.filter(id=id)

    @staticmethod
    def get_products_by_id(id):
        return Product.objects.filter(id__in=id)

    @staticmethod
    def get_all_products():
        return Product.objects.all()


# ------------------------------------------------------------------
# DISCOUNT MODEL
# ------------------------------------------------------------------

class Discount(models.Model):
    start_date = models.DateField(default=now)
    end_date = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    disc_per = models.PositiveIntegerField(default=None, validators=[MaxValueValidator(100), MinValueValidator(1)])

    class Meta:
        unique_together = ('start_date', 'end_date', 'product')

    # --------------------------------------------------------------

    def __str__(self):
        return str(self.start_date) + '-' + str(self.end_date) + '-' + str(self.product)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.update_discount()

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)
        self.update_discount()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.update_discount()

    @staticmethod
    def get_all_discounts():
        return Discount.objects.all()

    @staticmethod
    def cal_disc_price(per, price):
        return price - ((price/100) * per)

    @staticmethod
    def update_discount():
        discounts = Discount.get_all_discounts()
        products = Product.get_all_products()
        today = date.today()

        # Reset discounted prices of all products
        products.update(disc_price=None)

        # Apply discount on products if today is sale
        for discount in discounts:
            product = Product.get_product_by_id(discount.product.id)

            if (today >= discount.start_date) and (today <= discount.end_date):
                per = discount.disc_per
                price = discount.product.price

                disc_price = Discount.cal_disc_price(per, price)
                product.update(disc_price=disc_price)
            else:
                product.update(disc_price=None)


# ------------------------------------------------------------------
# ORDER MODEL
# ------------------------------------------------------------------

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = quantity = models.IntegerField()
    price = models.IntegerField()
    mode_of_payment = models.CharField(default='Cash On Delivery', max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    # --------------------------------------------------------------

    def __str__(self):
        return str(self.user) + '-' + str(self.price) + '-' + str(self.date)

    @staticmethod
    def get_orders_by_user(user_id):
        return Order.objects.filter(user=user_id).order_by('-date')
