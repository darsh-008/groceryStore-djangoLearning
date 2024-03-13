from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class item(models.Model):
    type = models.ForeignKey(Type, related_name="items", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=100)
    available = models.BooleanField(default=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    interested = models.PositiveIntegerField(default=0)

    def topup(self):
        return self.stock+50

    def __str__(self):
        return self.name


class Client(User):
    CITY_CHOICES = [('WD', 'Windsor'), ('TO', 'Toronto'), ('CH', 'Chatham'), ('WL', 'WATERLOO')]
    fullname = models.CharField(max_length=50)
    shipping_address = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=2, choices=CITY_CHOICES, default='CH')
    interested_in = models.ManyToManyField(Type)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.get_city_display()



class OrderItem(models.Model):
    # date_user = models.DateTimeField(auto_now=True)
    item = models.ForeignKey(item, on_delete=models.CASCADE, null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE,null=True, blank=True)
    quantity_ordered = models.PositiveIntegerField(default=1)
    ch_status = [(0, 'cancelled'),(1, 'placed'),(2, 'shipped'),(3, 'delivered')]
    status = models.IntegerField(choices=ch_status, default=1)
    last_updated = models.DateField(default=timezone.now)

    def __str__(self):
        return str(self.item)

    def total_price(self):
        return self.quantity_ordered * self.item.price

