from django.db import models
from store.models import User, Book


# Create your models here.

class Order(models.Model):
    pending = 'P'
    complete = 'C'
    Ordering_status = [
        (pending, 'Pending'),
        (complete, 'Complete')
    ]
    ordering = models.CharField(max_length=1, choices=Ordering_status)
    customer = models.ForeignKey(User, on_delete=models.PROTECT)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ManyToManyField(Book)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
