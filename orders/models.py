from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORIES = (
    ("RP", "Regular Pizza"),
    ("SP", "Sicilian Pizza"),
    ("SU", "Sub"),
    ("PA", "Pasta"),
    ("SA", "Salad"),
    ("DP", "Dinner Platter"),
)

SIZES = (
    ("S", "Small"),
    ("L", "Large")
)

class MenuItem(models.Model):
    category = models.CharField(max_length=64, choices=CATEGORIES, default="RP")
    name = models.CharField(max_length=64)
    size = models.CharField(max_length=64, choices=SIZES, blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
	    return f"{self.get_category_display()} - {self.name}: ${self.price} ({self.get_size_display()})"

class Topping(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Extra(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return f"{self.name}: ${self.price}"

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    toppings = models.CharField(max_length=128, blank=True)
    extras = models.CharField(max_length=128, blank=True)

    def __str__(self):
        if self.toppings != '':
            return f"{self.item} | Toppings: {self.toppings};"
        elif self.extras != '':
            return f"{self.item} | Extras: {self.extras};"
        else:
            return f"{self.item};"

STATUS = (
    ("P", "Pending"),
    ("C", "Completed")
)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_number = models.AutoField(primary_key=True)
    items = models.CharField(max_length=512)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=64, choices=STATUS, default="P")

    def __str__(self):
        return f"[Order no. {self.order_number}] {self.user} - ${self.total_price} ({self.get_status_display()})"
